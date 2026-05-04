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

Usage
python3 SnapSort.py

On first run, take one screenshot so SnapSort can detect your screenshot folder.

Setup Guide with Screenshots

