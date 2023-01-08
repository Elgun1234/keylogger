from main import keys
from deditor import edit
import threading
import time


def func1():
    k = keys()
def func2():
    time.sleep(2)
    e = edit()

x = threading.Thread(target=func1)
y = threading.Thread(target=func2)
x.start()
y.start()



