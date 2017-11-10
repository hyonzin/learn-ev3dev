#!/usr/bin/env python3

from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep
from threading import Thread
import random


btn = Button()
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

bark_mode = False


def bark(n=1):
    msg = ''
    for i in range(n):
        msg = msg+" mung"
    Sound.speak(msg).wait()


def random_bark():
    bark(n=random.randint(1, 3))


def bark_thread():
    global bark_mode
    while True:
        if bark_mode:
            random_bark()
        sleep(1)


""" functions for legs """


mh = MediumMotor("outC")
ml = LargeMotor("outD")
mr = LargeMotor("outA")


def walk(time_sp, speed_sp):
    ml.run_timed(time_sp=time_sp, speed_sp=speed_sp)
    mr.run_timed(time_sp=time_sp, speed_sp=speed_sp)


def sit_down():
    walk(time_sp=1000, speed_sp=100)


def stand_up():
    speed_sp = -300
    ml.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-30, stop_action="hold")
    mr.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-30, stop_action="hold")
    ml.wait_while("running")
    mr.wait_while("running")
    sleep(0.5)
    speed_sp = -400
    ml.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-34, stop_action="hold")
    mr.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-34, stop_action="hold")
    ml.wait_while("running")
    mr.wait_while("running")
    sleep(0.5)
    speed_sp = -300
    ml.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-40, stop_action="hold")
    mr.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-40, stop_action="hold")
    ml.wait_while("running")
    mr.wait_while("running")
    sleep(0.5)
    speed_sp = -50
    ml.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-60, stop_action="hold")
    mr.run_to_abs_pos(speed_sp=max(speed_sp, -1000), position_sp=-60, stop_action="hold")
    ml.wait_while("running")
    mr.wait_while("running")


""" main code """


def on_button_up(state):
    if not state:
        return
    lcd_show("Button Up")


def on_button_down(state):
    if not state:
        return
    lcd_show("Button Down")


def on_red():
    lcd_show("Red")
    sit_down()


def on_yellow():
    lcd_show("Yellow")
    stand_up()


def on_green():
    lcd_show("Green")
    speed_sp = 800
    time_sp = 400
    mh.run_timed(speed_sp=-speed_sp, time_sp=time_sp)
    mh.wait_while("running")
    mh.run_timed(speed_sp=speed_sp, time_sp=time_sp)
    mh.wait_while("running")
    mh.run_timed(speed_sp=-speed_sp, time_sp=time_sp)
    mh.wait_while("running")
    mh.run_timed(speed_sp=speed_sp, time_sp=time_sp)
    mh.wait_while("running")


def on_blue():
    global bark_mode
    bark_mode = False   # not bark_mode
    if bark_mode:
        lcd_show("Blue (True)")
    else:
        lcd_show("Blue (False)")


def init():
    global btn
    btn.on_up = on_button_up
    btn.on_down = on_button_down
    sit_down()
    sit_down()
    sit_down()
    ml.wait_while("running")
    mr.wait_while("running")
    ml.reset()
    mr.reset()


def start():
    t = Thread(target=bark_thread)
    t.start()
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
