import keyboard as kb
from time import sleep
from random import randint
from random import choice
start = False
def enterKeys():
    for i in range(randint(0,15)):
        for o in choice(('elephant','purple','jazz','breeze','carousel','whisper','marathon','quasar','umbrella','xylophone','nectar','galaxy','blizzard','trampoline','pyramid')):
            kb.press_and_release(o)
            sleep(randint(1,5) / 10)
        kb.press_and_release("space")
    kb.press_and_release('enter')
    sleep(randint(10,15))
    kb.press_and_release('ctrl+w')
    sleep(0.1)
    kb.press_and_release('ctrl+t')
while True:
    if kb.is_pressed("`"):
        start = True
        break
for i in range(30):
    enterKeys()