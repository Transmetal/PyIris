# The PyIris Project (Updates coming soon refer to ROADMAP.md)
The PyIris project is a modular remote access trojan toolkit written completely in python.
It allows users to dynamically build, generate and encode/encrypt remote access trojan payloads for remote
control of other compromised hosts.

# Features (Both Windows and Linux)
- Tab completion for most commands
- Dynamically generate scouts
- Robust error handling to allow scouts to recover from sudden disconnects
- Upload and download files from and to the target machine
- Sleep, kill and disconnect scouts
- Download files from external urls (web dowloads)
- Keylogging in memory
- Displaying system information
- Taking screenshots without writing to disk
- See all currently open visible and non visible windows on the target
- Check to see if scout is running with admin/root privileges
- Inject keystrokes
- Compile payloads into Windows EXEs or Linux ELFs
- Clear, set or dump clipboard data
- Setting audio
- Take pictures from webcam without writing to disk
- Stackable encryption of scout payload source code, in a theoretically infinite stack in infinite variations
- execute arbitrary python code and read the results even if the python interpreter is not installed on the target machine from compiled 
scouts
- request for admin/root
- sleep for an arbitrary length of time before running (To bypass AV dynamic program analysis)
- self delete (only works for scripts)
- Stream webcam over TCP sockets (pretty laggy will work on a UDP version)

# Features (Windows)
- Acheive persistence through the windows registry (HKEY_CURRENT_USER)
- Acheive persistence through the windows startup folder
- Remote Command Execution through cmd.exe or powershell.exe (provided it is not blocked)
- Open URLs from native browser (internet explorer ewww)
- Shutdown, restart, lock, logoff user gracefully without connection hanging from scout payload
- Execute or open files remotely
- Check the user idle time
- Dump saved chrome passwords (wont work with the latest chrome browsers since they changed encryption methods and Im kinda lazy to update this lol)
- Disbale/ Enable the targets keyboard/mouse
- Bypass UAC through sdclt.exe (Has already been patched in recent windows updates)

# Features (Linux)
- Achieve persistence through cron jobs (crontab)
- Remote Command Execution through the bash shell

# Getting Started
## Prerequisites
- Python 3.x, (I use python 3.7.x)
- Git

## Setting up PyIris (Windows)

First, clone this repository (make sure you have git installed), CD into the root folder.

```git clone https://github.com/Transmetal/PyIris```

```cd PyIris-backdoor```

Next install the rest of the required modules with pip3. Only install modules from the ```setup/windows/requirements.txt``` file
as this section is for running the Windows edition of PyIris.

```pip3 install -r setup/windows/requirements.txt```

Upon running ```PyIris.py``` in the root folder for the first time you should be greeted with the option to generate a key, this indicates everything has been installed
correctly.

## Setting up PyIris (Linux)

First, clone this repository (make sure you have git installed), CD into the root folder.

```git clone https://github.com/Transmetal/PyIris```

```cd PyIris-backdoor```

Next install an external dependency, xlib, required by pyperclip through apt-get.

```sudo apt-get install xclip```

Then install pyalsaaudio through apt-get, if you're installing on **ubuntu** please read the below note

```sudo apt-get install python3-alsaaudio```

After that install canberra-gtk-module for cv2 to use to display webcam live streams

```sudo apt-get install libcanberra-gtk-module```

Pyautogui refuses to be imported in linux if tkinter is not installed so we must install it. However, we are not actually using tkinter
for any of the scouts

```sudo apt-get install python3-tk python3-dev``` 

Finally, install the rest of the required modules with pip3. Only install modules from the ```setup/linux/requirements.txt``` file as
this section is for running the Linux edition of PyIris.

```pip3 install -r setup/linux/requirements.txt```

Upon running it the first time you should be greeted with the option to generate a key, this indicates everything has been installed
correctly.

## Updating PyIris
Change into the PyIris-backdoor folder first, then run

```git pull```

On windows to install any newly added third party modules or update then run

```cd setup/windows```

```pip3 install -r requirements.txt```

On linux to install any newly added third party modules or update then run

```cd setup/linux```

```pip3 install -r requirements.txt```

## Supported OS
### PyIris was successfully installed on the following operating systems
- Windows 10
- Kali Linux Rolling releases
- Ubuntu
- Debian

# Basic Usage
## Windows

```py -3 PyIris.py```

If prompted to generate a key, either press enter or enter a key that you want to use.

## Linux

```python3 PyIris.py```

If prompted to generate a key, either press enter or enter a key that you want to use.

## Starting out
The ```help``` command is your friend! Simply run ```help``` to get a list of all commands you can use on a specific interface. For more 
detail about a specific command, run ```help <name of command>``` to get more in depth help about it. Alternatively you can use the 
```?``` command which is an alias for the help command. I am planning to write a wiki soon detailing all the commands and information
you need to use PyIris
