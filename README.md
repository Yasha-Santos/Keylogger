# Keylogger

"KeyLog.txt" file contents example:

![](/Images/KeyLog_Image_file.png)


### Description of the Keylogger

A keylogger is used as malicious software used to record all the keystrokes in a user in hopes of using all the information recorded in the "KeyLog.txt"(or named any kind) file, for malicious intent
This keylogger software is made to get a copy of each keystroke of a user. The keystroke format is shown as a ".txt" file formatted as (TIME/DATE:KEYSTROKE).
This software is made for educational purposes only! Use it at your discretion.

*This software won't work in an attack because the computer antivirus already has a signature for this kind of code*


This is the keylogger file:
- [Keylogger](https://github.com/Yasha-Santos/Keylogger/blob/main/Keylogger.py)
*The code above contains comments on how it works, minimal explanation will be provided*

Basically what this code does is that it saves all the keystrokes of a user in a running environment, meaning that it is not a one-time use only as it uses a thread to maintain its "life", meaning that when this file is executed a user won't notice a difference but in the background, it will be using a single process to capture every possible keystrokes or combination.

This is a small example of what the keylogger will record.
- [Keylog.txt (Example file)](https://github.com/Yasha-Santos/Keylogger/blob/main/KeyLog.txt)

The keylogger can store more information in this file, as long as the user is writing this software will record every single keystroke. The file above is only an example of what the output will look like.
