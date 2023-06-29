import mouse
import keyboard
import os
from dotenv import load_dotenv
import time

load_dotenv()

MOUSE_CLICK = os.getenv('MOUSE_CLICK')
START_BUTTON = os.getenv('START_BUTTON')
FINISH_BUTTON = os.getenv('FINISH_BUTTON')


def mouseClick():
    exit = False
    while not exit:
        mouse.click(MOUSE_CLICK);
        time.sleep(0.01)
        exit = keyboard.is_pressed(FINISH_BUTTON)

while True:
    keyboard.wait(START_BUTTON)
    mouseClick()
    print('finish')