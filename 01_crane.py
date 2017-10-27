#!/usr/bin/env python3


from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep

lcd = Screen()
ts = TouchSensor()
cs = ColorSensor()
btn = Button()

motor = {
    "A": MediumMotor('outA'),
    "B": LargeMotor('outB'),
    "C": LargeMotor('outC'),
}

#cs.mode = 'COL-COLOR'
cs.mode = 'COL-REFLECT'

COLORS = ['unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown']


""" functions for LCD """

def lcd_show(str):
    lcd.clear()
    lcd.draw.text((60,60), str, font = fonts.load('luBS24'))
    lcd.update()


""" functions for motor """

def motor_move(idx, pos, speed=200):
    motor[idx].run_to_abs_pos(
        position_sp=pos,
        speed_sp=speed,
        stop_action='brake')
    motor_wait(idx)

def motor_wait(idx):
    motor[idx].wait_while("running")

def goto(area):
    if area >= 0 and area <= 2:
        pos = -320 * area
        motor_move("C", pos)

def up():
    #motor_move("B", 0)
    while cs.value() < 20:
        motor["B"].run_forever(speed_sp=-200)
    motor["B"].stop()

def middle():
    motor_move("B", 300)

def down():
    motor_move("B", 400)

def fold():
    motor_move("A", 80)

def unfold():
    motor_move("A", 0)


""" functions for Crane Application """

def init():
    goto(1)
    up()
    unfold()

def on_button_up():
    goto(2)
    down()
    fold()
    middle()
    goto(1)
    down()
    unfold()
    up()
    goto(1)

def on_button_down():
    goto(0)
    down()
    fold()
    middle()
    goto(1)
    down()
    unfold()
    up()
    goto(1)

init()
btn.on_up = on_button_up
btn.on_down = on_button_down