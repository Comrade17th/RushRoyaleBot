import pyautogui as pag
import time as t

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1280
# делать -1023 в фотошопе, чтобы получить точку для питона

# returns the coords of dot
# where mause cursor located (x=984, y=848)
def get_coord():
    t.sleep(2.5)
    return(pag.position())

def move_to(dot):
    pag.moveTo(dot.x, dot.y)
    