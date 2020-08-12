from pynput.keyboard import Key, Controller
from time import sleep

def kh_warnings(iterations):
    keyboard = Controller()
    counter = 0
    messages = ['TNT ~ Tents Next Turn\n', 'D1 ~ Down on 1\n', 'D2 ~ Down on 2\n', 'OOZ ~ Out Of Zone\n']
    down = down_select()

    # Performs warnings on current active window
    while counter < iterations:
        countdown(60)
        bait_and_switch(keyboard, messages[0])
        countdown(20)
        bait_and_switch(keyboard, messages[3])
        countdown(20)
        bait_and_switch(keyboard, messages[down])
        counter += 1

def countdown(time):
    while time > 0:
        print(f'Next Warning In: {time} seconds\r', end="")
        time -= 1
        sleep(1)

def down_select():
    while True:
        try:
            down = int(input('What Down is it? (1/2): '))
            if down == 1 or down == 2:
                return down
            else:
                print("Please input a 1 or 2!")
        except ValueError:
            print("Invalid Input! Please select an integer!")

def bait_and_switch(keyboard, message):
    # Highlight All
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    keyboard.type(message)
    # Pastes Saved Message
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

if __name__ == '__main__':
    kh_warnings(18)
