# PASSWORD LOCKER

This is a command line application built with python3.6 that gives the user the ability to create or generate passwords for various applications and websites that the user has been granted access to and securely store them.

# prerequisites

* python3.6 is installed in your operating system.
* Pyperclip is installed and properly configured. 

## installation process

* clone this [repository](https://github.com/gichimux/password-locker)
* Download pyperclip.
* If on linux, type ```$ sudo apt install xsel``` on your terminal to configure pyperclip .
* Type ``` python3.6 run.py ``` in your terminal.


### How it works

The application uses simple shortcodes to enable the user access the various functionalities in the application

before account creation, this are the shortcodes used 


short code| result expected       
----------------------------------      
    'ca'    | Creates a new account 
    'ln'    | Logs user in  
    'ex'    | Exits the application 

After account creation these shortcodes provided enable more functionality

short code| result expected
----------------------------
    'ac'    | adds account Credentials 
    'vc'   | views Credentials for the named app
    'cp'   | Copies an application Password to the clipboard
    'lo'   | Logs Out User
    'dc'   | Deletes a named Credential

# TECHNOLOGIES USED

the application is made using python 3.6

# Author

This application was made by george gichimu
to report bugs or make contact, reach me on this email address: [gichimu.dev@gmail.com](gichimu.dev@gmail.com)

# Application url

[Password Locker](https://github.com/gichimux/password-locker)

# Bugs reported

Pyperclip bugs on previous version have been fixed.
No bugs reported.

