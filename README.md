# Installation

## ----------- Installation ----------
#### !Currently working only on Arm64 (mac silicon) and with chrome! 
#### !Download chromedriver and make sure that your chrome browser and chromedriver are the same version!
#### !To make it work with your browser (Firefox or Chrome) you need to download the correct webdriver and make sure to direct the path to it!

## ---------- Dependencies install -------
### Please install the dependencies first
#### 1. Create the Virtual Enviroment
#### - python -m venv .<insert>name
#### - activate the venv source .<insert>name/bin/activate (macos) || source .<insert name>/scripts/activate (windows)
#### - In terminal install depencencies pip install -r requirements.txt

## --------- Set Path --------
#### On line 8: Make sure that you are directing the path to where your chromedriver is!
#### Example:
#### CHROMEDRIVER_PATH = "/path/user/Downloads/chromedriver-mac-arm64/chromedriver"  

#### On line 9: Make sure that you paste the right url into this path
#### TICKETMASTER_URL = "https://www.ticketmaster.de/event/event"  


## --------- Language change --------
#### Lastly, on both line 21 and 29, you have the xpath span text.
#### Tickets and Erneut versuchen, change those to whatever it says on your ticketmaster side. In your case it could be "Tickets" and "Try again" or "Biljetter" and "Försök igen". 


## TEST THE TOOL 
#### If it works, create an Executable

#### In the terminal write: 
#### pyinstaller --onefile ticketmaster.py
#### A new folder called Dist will be created in your directory. You'll find the .exe there, open it and see the magic happens.