import os
import time
import json
import shutil
import subprocess
from pathlib import Path

BASE = Path("/storage/emulated/0")
CONFIG = Path.home() / ".screenshot_sorter.json"
DEST_BASE = BASE / "DCIM"


def load_config():
    if CONFIG.exists():
        return json.loads(CONFIG.read_text())

    return {
        "watch_folder": None,
        "folders": []
    }


def save_config(config):
    CONFIG.write_text(json.dumps(config, indent=2))


def latest_image():
    images = []

    for root, dirs, files in os.walk(BASE):
        for name in files:
            if name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                path = Path(root) / name
                try:
                    images.append(path)
                except PermissionError:
                    pass

    if not images:
        return None

    return max(images, key=lambda p: p.stat().st_mtime)


def load_watch_folder(config):
    saved = config.get("watch_folder")

    if saved:
        path = Path(saved)
        if path.exists():
            return path

    print("Take a screenshot now so I can detect your screenshot folder...")

    before = latest_image()

    while True:
        time.sleep(1)
        after = latest_image()

        if after and after != before:
            folder = after.parent
            config["watch_folder"] = str(folder)
            save_config(config)
            print(f"Detected screenshot folder: {folder}")
            return folder


def get_existing_folders():
    if not DEST_BASE.exists():
        DEST_BASE.mkdir(parents=True, exist_ok=True)

    return sorted([
        p.name for p in DEST_BASE.iterdir()
        if p.is_dir()
    ])


def ask_radio(title, options):
    result = subprocess.check_output([
        "termux-dialog",
        "radio",
        "-t", title,
        "-v", ",".join(options)
    ])

    return json.loads(result.decode()).get("text")


def ask_text(title, hint):
    result = subprocess.check_output([
        "termux-dialog",
        "text",
        "-t", title,
        "-i", hint
    ])

    return json.loads(result.decode()).get("text", "").strip()


def choose_folder(config):
    folders = config.get("folders", [])

    options = folders + ["+keep in screenshots", "+create new", "+select existing folder"]

    choice = ask_radio("Move Screenshot", options)

    if not choice:
        return None
    
    if choice == "+keep in screenshots":
        return "KEEP_ORIGINAL"

    if choice == "+create new":
        new_folder = ask_text("New Folder Name", "folder_name")

        if not new_folder:
            return None

        dest = DEST_BASE / new_folder
        dest.mkdir(parents=True, exist_ok=True)

        if new_folder not in folders:
            folders.append(new_folder)
            config["folders"] = folders
            save_config(config)

        return new_folder

    if choice == "+select existing folder":
        existing = get_existing_folders()

        if not existing:
            return None

        selected = ask_radio("Select Existing Folder", existing)

        if not selected:
            return None

        if selected not in folders:
            folders.append(selected)
            config["folders"] = folders
            save_config(config)

        return selected

    return choice


config = load_config()
watch_folder = load_watch_folder(config)
known = set(os.listdir(watch_folder))

print(f"Watching: {watch_folder}")

def safe_move(src, dest_folder):
    dest = dest_folder / src.name

    if not dest.exists():
        shutil.move(str(src), str(dest))
        return dest

    stem = src.stem
    suffix = src.suffix
    counter = 1

    while True:
        new_dest = dest_folder / f"{stem}_{counter}{suffix}"

        if not new_dest.exists():
            shutil.move(str(src), str(new_dest))
            return new_dest

        counter += 1

while True:
    current = set(os.listdir(watch_folder))
    new_files = current - known

    for file in new_files:
        src = watch_folder / file

        if not src.is_file():
            continue

        choice = choose_folder(config)
        
        if choice == "KEEP_ORIGINAL":
            known.add(file)
            continue
        if not choice:
            known.add(file)
            continue

        dest = DEST_BASE / choice
        dest.mkdir(parents=True, exist_ok=True)

        moved_to = safe_move(src, dest)
        print(f"Moved {file} -> {moved_to}")

    known = current
    time.sleep(2)