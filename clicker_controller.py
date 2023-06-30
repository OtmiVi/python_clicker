import mouse
import keyboard
import os
from dotenv import load_dotenv
import time

class ClickerController:

    def __init__(self) -> None:
        load_dotenv()
        self.MOUSE_CLICK = os.getenv('MOUSE_CLICK')
        self.START_BUTTON = os.getenv('START_BUTTON')
        self.FINISH_BUTTON = os.getenv('FINISH_BUTTON')

    def run(self) -> None:
        while True:
            keyboard.wait(self.START_BUTTON)
            self.__mouseClick()
            print('finish')

    def __mouseClick(self) -> None:
        exit = False
        while not exit:
            mouse.click(self.MOUSE_CLICK);
            time.sleep(0.01)
            exit = keyboard.is_pressed(self.FINISH_BUTTON)
