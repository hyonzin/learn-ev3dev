from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts

lcd = Screen()
btn = Button()

melody = ('do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do')
freq = (523, 587, 659, 698, 784, 880, 988, 1047)
comb = (
    ['left'], ['up'], ['right'], ['down'],
    ['left','up'], ['up','right'], ['right','down'], ['down','up']
)
lcd_str=''

def gonban(melody_num):
    global lcd_str
    Sound.tone(freq[melody_num], 200).wait()
    lcd_str += melody[melody_num] + '-'

def update_screen():
    global lcd_str
    lcd.clear()
    lcd.draw.text((5,5), lcd_str, font = fonts.load('luBS18'))
    lcd.update()

while True:
    for i in range(0, 8):
        if btn.check_buttons(buttons=comb[i]):
            gonban(i)
            update_screen()
    sleep(0.01)
