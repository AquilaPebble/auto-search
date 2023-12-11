import keyboard as kb
from time import sleep
from random import randint
from random import choice
searchOn = False
def enterKeys():
    for o in range(randint(5,12)):
        kb.press_and_release(choice([str(i) for i in range(0,10)] + list("abcdefghijklmnopqrstuvwxyz")))
    kb.press_and_release('enter')
    sleep(randint(3,5))
    kb.press_and_release('ctrl+w')
    sleep(0.1)
    kb.press_and_release('ctrl+t')
while True:
    if kb.is_pressed("`"):
        searchOn = not searchOn
        sleep(0.1)
    if searchOn:
        enterKeys()