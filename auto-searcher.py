import keyboard as kb
from time import sleep
from random import randint
from random import choice
searchOn = False
def enterKeys():
    for o in range(randint(0,15)):
        kb.press_and_release(choice(['elephant','purple','jazz', 'breeze','carousel','whisper','marathon','quasar','umbrella','xylophone','nectar','galaxy','blizzard','trampoline','pyramid']) + ' ')
    kb.press_and_release('enter')
    sleep(randint(4,5))
    kb.press_and_release('ctrl+w')
    sleep(0.1)
    kb.press_and_release('ctrl+t')
while True:
    enterKeys()