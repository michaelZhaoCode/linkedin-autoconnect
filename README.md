# LinkedIn Autoconnect
Finds LinkedIn profile links from a body of text and automatically sends connection requests using your account.
# How to Use
First enter LinkedIn login information and a connection message into the variables in `linkedin_constants.py`.  
Then, paste body of text containing LinkedIn links into `messages.txt` and then run.  
The program will find all the links, clean them, and then go to all of them and send connection requests.  
The status of the current operation is printed out to the user.
# Notes
-Note that auto login will not work if you use login verification so you can insert a sleep command to login manually. This will require you to disable the headless chromeoptions.  
-Note that the cleaner for link texts is not that strong so if the link has extra text on it, e.g. parentheses, then it will require manual cleaning.  
-Note that no data is retrieved from LinkedIn, the website is only read to find the buttons required.
# Requirements
To install, run `pip install <module>`  
- `selenium` - Version 4.4.3:  https://www.selenium.dev  
- `undetected-chromedriver` - Version 3.1.5.post4: https://github.com/ultrafunkamsterdam/undetected-chromedriver  
