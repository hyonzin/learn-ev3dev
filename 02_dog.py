from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep
import random


cs = ColorSensor()
cs.mode = 'COL-COLOR'

COLORS = ['unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown']
COLOR_BLUE = 2
COLOR_GREEN = 3
COLOR_YELLOW = 4
COLOR_RED = 5

""" functions for LCD """

lcd = Screen()


def lcd_show(str):
    lcd.clear()
    lcd.draw.text((5,60), str, font = fonts.load('luBS24'))
    lcd.update()


""" functions for dog barking"""


def make_bark_sound():
    sound = []
    for i in range(8):
        sound.append((500-i*10, 10, 0))
    return sound


def bark(sound=make_bark_sound(), N=1):
    for i in range(N):
        Sound.tone(sound)


def random_bark(sound=make_bark_sound()):
    bark(sound, N=random.randint(1,4))


bark_sound = make_bark_sound()


""" functinos for legs """


mh = MediumMotor("outC")
ml = LargeMotor("outD")
mr = LargeMotor("outA")


def walk(time, speed):
    ml.run_timed(time_sp=time, speed_sp=speed)
    mr.run_timed(time_sp=time, speed_sp=speed)


def sit_down():
    ml.run_timed(time_sp=1000, speed_sp=100)
    mr.run_timed(time_sp=1000, speed_sp=100)


def stand_up():
    ml.run_timed(time_sp=330, speed_sp=-400)
    mr.run_timed(time_sp=330, speed_sp=-400)


stand_up()
sleep(2)

sit_down()


""" main code """

btn = Button()


def on_red():
    lcd_show("Red")
    bark(bark_sound)


def on_button_up(state):
    if not state:
        return
    lcd_show("Button Up")


def on_button_down(state):
    if not state:
        return
    lcd_show("Button Down")


def on_yellow():
    lcd_show("Yellow")


def on_green():
    lcd_show("Green")


def on_blue():
    lcd_show("Blue")


def init():
    global btn
    btn.on_up = on_button_up
    btn.on_down = on_button_down


def start():
    while True:
        sleep(0.5)
        # on button
        btn.process()
        # on color sensor
        cs_value = cs.value()
        if cs_value == COLOR_RED:
            on_red()
        elif cs_value == COLOR_YELLOW:
            on_yellow()
        elif cs_value == COLOR_GREEN:
            on_green()
        elif cs_value == COLOR_BLUE:
            on_blue()

init()
start()
