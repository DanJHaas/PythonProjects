from pynput import keyboard
from pynput.keyboard import Key, Controller
message = []
yes = Controller()
def here():
    return True

def on_press(key):
    letter = str(key).replace("'","")
    if key == keyboard.Key.esc:
        for i in range(len(message)):
            yes.press(Key.backspace)
            yes.release(Key.backspace)
        for i in range(len(message)):
            yes.type(message[i])
        return False
    if(key == Key.space):
        message.append("    ")
    if(key == Key.space or key == Key.enter or key == Key.shift):
        print("")
    else:
        message.append(":regional_indicator_"+str(letter)+": ")
        
lis = keyboard.Listener(on_press=on_press)
lis.start()
lis.join()

