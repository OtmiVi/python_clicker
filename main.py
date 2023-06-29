import mouse
import keyboard

def mouseClick():
    exit = False
    while not exit:
        #mouse.click('right')
        print('click')
        exit = keyboard.is_pressed('a')

#keyboard.add_hotkey('k', mouseClick)

while True:
    keyboard.wait("k")
    mouseClick()
    print('finish')