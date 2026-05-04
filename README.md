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

**Step 1: Update Termux packages**
Run `pkg upgrade`


<img width="297" height="293" alt="image" src="https://github.com/user-attachments/assets/d1615269-8b61-4bc2-beca-25c23696fb57" />


**Step 2: Install required packages**
Run `pkg install termux-api python`. This installs Python and the Termux API needed for popups.


<img width="300" height="435" alt="image" src="https://github.com/user-attachments/assets/28b49044-33da-41e9-8a49-c7b298881812" />


**Step 3: Install Termux:API from F-Droid**  
This app enables popups and Android features (like dialogs) from Termux. It must be installed for the script to work.


<img width="296" height="614" alt="image" src="https://github.com/user-attachments/assets/6cc160fe-0dd2-4a68-89a6-5300d2e6d67d" />


**Step 4: Open App Settings**  
Go to your phone’s **Settings → Apps** to manage permissions for Termux:API.


<img width="294" height="622" alt="image" src="https://github.com/user-attachments/assets/fb3cb244-7f06-4da5-a94d-aa0de0173679" />


**Step 5: Find Termux:API**  
Scroll through the apps list (or use the search icon) and select **Termux:API**.


<img width="290" height="601" alt="image" src="https://github.com/user-attachments/assets/4e098b36-ed3b-4794-b45d-7485c329ad9a" />


**Step 6: Enable “Appear on top”**  
Scroll down and tap **Appear on top** for Termux:API. This allows popups to show over other apps.
Then scroll down until you see Appear On Top and click on it:


<img width="300" height="553" alt="image" src="https://github.com/user-attachments/assets/b6c04528-868c-47bc-9a01-76912014ec58" />


**Step 7: Turn it on**  
Enable the toggle to allow Termux:API to display popups on your screen.


<img width="302" height="224" alt="image" src="https://github.com/user-attachments/assets/9df1fd1e-41c8-4c4b-8198-e0aade21b4d1" />


**Step 8: Set battery usage to Unrestricted**  
Go back to **Termux:API → Battery** and choose **Unrestricted** so the popup service does not get killed in the background.


<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/7d8f3d47-6b1c-4c9e-9863-03c849a662d3" />


**Step 9: Give Termux storage access**  
Go back to Termux and run `termux-setup-storage`. This lets Termux access Android storage and creates the `~/storage` folder shortcuts.


<img width="301" height="26" alt="image" src="https://github.com/user-attachments/assets/07bdf445-a8ff-42c2-9dca-77f711daac25" />


**Step 10: Locate and run the script**
There is two options to locate and run the script:


**Option 1:** Use the `cd` command to navigate to the folder where the downloaded Python file is located, then use the `cp` command to copy it into the main Termux directory.


First, check your default directory using `pwd`.


<img width="301" height="42" alt="image" src="https://github.com/user-attachments/assets/fb265f6a-fb46-4873-b5c2-4699eb4bd236" />


**Next, navigate to your device storage**  
Run `cd storage` to access your Android storage folders (Downloads, DCIM, Pictures, etc.).


<img width="256" height="32" alt="image" src="https://github.com/user-attachments/assets/0bc4c407-e409-445f-a151-033da1aad640" />


**Navigate to Downloads and copy the script**  
Use `cd downloads` to go to your Downloads folder where the Python file is located.


Then run `cp screenshot-sorter1.py /data/data/com.termux/files/home/` to copy it to your Termux home directory.


<img width="300" height="42" alt="image" src="https://github.com/user-attachments/assets/32103aa6-fa81-4cda-8c1f-3f8b1f01953d" />


**Option 2: Use your file explorer**  
Open your file explorer and locate the downloaded Python file. Tap **Open with → Termux**.


You’ll be prompted to save it to the Termux downloads folder (this is Termux’s private storage).

Then open Termux, use the `cp` command to copy the file to your main Termux directory, and run it from there for easy access anytime.


**First, open your file explorer**, locate the Python file, tap the three-dot menu, and select **Open with**.


<img width="170" height="316" alt="image" src="https://github.com/user-attachments/assets/e33d0a9d-13e3-4126-8207-058c8820439e" />


Then select **Termux**. You can choose “Always” if you want, but it’s not required.


<img width="152" height="171" alt="image" src="https://github.com/user-attachments/assets/faf11994-41f1-4fb3-bf46-3698ab1ac9ff" />


A popup will appear asking to save the file in `~/downloads`. Tap **Open Directory**.

Note: this is Termux’s private downloads folder, not your device’s main Downloads folder.


<img width="287" height="219" alt="image" src="https://github.com/user-attachments/assets/715c7828-93f1-4720-97d1-54c4d21eeb70" />


Termux will open in its private `~/downloads` folder. From here, use the `cp` command to copy the Python file into your main Termux home directory


<img width="299" height="222" alt="image" src="https://github.com/user-attachments/assets/013cbe2d-ed5e-49c6-9a10-d705316f9abf" />


**Step 11: Run SnapSort**  
Run the Python file. On the first launch, it will ask you to take one screenshot so it can detect your default screenshot folder.

After that, it will keep watching that folder. When you take a new screenshot, it will ask which folder you want to move it to.


<img width="1080" height="272" alt="image" src="https://github.com/user-attachments/assets/35680a59-88b8-4cd6-83e5-9349447bbcba" />


**Step 12: Choose where to move the screenshot**  
After taking a new screenshot, a popup appears. You can choose to keep it in the screenshots folder, create a new folder, or select an existing folder from your device.


<img width="263" height="288" alt="image" src="https://github.com/user-attachments/assets/5090c5a3-923b-466d-a0a1-f09c6e93f3a5" />


If you choose **create new**, you’ll be prompted to enter a folder name. After tapping **OK**, the folder is created and added to the menu for future screenshots.


<img width="257" height="178" alt="image" src="https://github.com/user-attachments/assets/8c7ce07c-41e6-4e65-8bfa-f31cfd8b3662" />


<img width="939" height="643" alt="image" src="https://github.com/user-attachments/assets/e839e94a-ac55-4025-b6e9-64f6d16ce3d2" />


If you choose **select existing folder**, it will show the folders inside your device’s `DCIM` folder. Select one and tap **OK**. The screenshot will be moved there, and that folder will be saved in the menu for next time.


<img width="277" height="601" alt="image" src="https://github.com/user-attachments/assets/90431739-2b5e-497b-89be-bd2505d400cd" />


**Note:** Selecting **keep in screenshots** will leave the screenshot in the detected screenshots folder. It won’t be moved, and the script will stop prompting for that file.























