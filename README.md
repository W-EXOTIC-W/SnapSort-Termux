# SnapSort-Termux

Automatically sort Android screenshots with interactive popups using Termux.

## What it does

SnapSort-Termux watches your Android screenshot folder. When you take a screenshot, it shows a popup that lets you:

- Keep it in Screenshots
- Move it to a new folder
- Move it to an existing folder

## Requirements

- Termux
- Termux:API app
- Python
- Storage permission

## Installation

```bash
pkg update
pkg install python termux-api
termux-setup-storage
```

## Usage
```
python3 SnapSort.py
```

On first run, take one screenshot so SnapSort can detect your screenshot folder.

## Setup Guide with Screenshots

Step 1: Update Termux packages
Run `pkg upgrade`

<img width="297" height="293" alt="image" src="https://github.com/user-attachments/assets/d1615269-8b61-4bc2-beca-25c23696fb57" />

Step 2: Install required packages
Run `pkg install termux-api python`. This installs Python and the Termux API needed for popups.

<img width="300" height="435" alt="image" src="https://github.com/user-attachments/assets/28b49044-33da-41e9-8a49-c7b298881812" />

**Step 3: Install Termux:API from F-Droid**  
This app enables popups and Android features (like dialogs) from Termux. It must be installed for the script to work.



