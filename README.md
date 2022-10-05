# LinkedIn Autoconnect
Finds linkedin profile links from a body of text and automatically sends connection requests using your account.
# How to Use
First enter LinkedIn login information into the variables in `linkedin_constants.py`. Note that auto login will not work if you use login verification so you can insert a sleep command to login manually.  
Then, paste body of text containing LinkedIn links into `messages.txt` and then run.  
The program will find all the links, clean them, and then go to all of them and send connection requests.
# Requirements
To install, run `pip install <module>`  
- `selenium` - Version 4.4.3:  https://www.selenium.dev  
- `undetected-chromedriver` - Version 3.1.5.post4: https://github.com/ultrafunkamsterdam/undetected-chromedriver  
