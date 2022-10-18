import time
import win32api, win32con
from random import *
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

try:
    while True:
        x = randint(1, 1000)
        y = randint(1, 1000)
        click(x,y)
        time.sleep(10)
except KeyboardInterrupt:
    print('interrupted!')