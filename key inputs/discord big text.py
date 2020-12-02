from re import match
from pynput import keyboard
from pynput.keyboard import Key, Controller
import re

### setup for variables and structs
message = []
yes = Controller()
regstr = r"[a-z]"
regnum = r"[0-9]"
numbers={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

### main keypress def
def on_press(key):
    ### cleanup the input coming in from [key]
    letter = str(key).replace("'","")

    ### typing out the result stored in an array
    if key == keyboard.Key.esc:
        ### delete the original message
        for i in range(len(message)):
            yes.press(Key.backspace)
            yes.release(Key.backspace)
        ### retype the new one
        for i in range(len(message)):
            yes.type(message[i])
        return False

    ### use regex to figure out keys, looks cleaner
    if key == Key.space:
        message.append("    ")
    ### looking for letters
    elif bool(re.match(regstr, letter)):
        message.append(":regional_indicator_"+str(letter)+": ")
    ### looking for numbers
    elif bool(re.match(regnum, letter)):
        message.append(":{0}: ".format(numbers.get(letter)))
    ### print something when any other key is pressed
    else:
        print("no key")

### keyboard listener stuff
lis = keyboard.Listener(on_press=on_press)
lis.start()
lis.join()