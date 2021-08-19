from pynput.keyboard import Key, Controller
from random import randint
from time import sleep

keyboard = Controller()

if __name__ == "__main__":

    while True:
        with keyboard.pressed(Key.shift):
            sleep(0.2)
        sleep(randint(1,2) / 4)
