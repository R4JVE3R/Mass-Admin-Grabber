# Mass-Admin-Grabber

## Overview:
Mass Admin Grabber is Tool developed in python3 and it uses Library called urllib3.
It Used to find admin panel of more than one website at a time.
To use this tool you have to provide list of websites and it will find admin panel of all those sites if it exists.
    
## Requirements:
- Python3
- urllib3
- colorama

## Usage:
There is File list.txt, So you have to provide your list of websites in this file.
#### Example:
    xyz.com
    abc.com
    ijk.com

Now just run the script but notice one thing if you have installed multiple version of python on your system then 
You have to specify version 3 of python to run the script.
#### Example:
    python3 MassAdminGrabber.py

Or else if you have only installed python3 on your system then you can directly run the script.
#### Example: 
    python MassAdminGrabber.py

After Execution you will get Result.txt in which you will get all websites found with their admin panel
