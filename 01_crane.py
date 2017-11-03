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

COLORS = ['unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown']
COLOR_BLUE = 2
COLOR_GREEN = 3
COLOR_YELLOW = 4
COLOR_RED = 5


""" functions for LCD """

def lcd_show(str):
    lcd.clear()
    lcd.draw.text((60,60), str, font = fonts.load('luBS24'))
    lcd.update()


""" functions for motor """

global current_b


def motor_init():

    # initial
    while cs.value() < 20:
        motor["B"].run_forever(speed_sp=-50)
    motor["B"].stop()

    motor["A"].run_timed(time_sp=1000, speed_sp=200)

    while not ts.is_pressed:
        motor["C"].run_forever(speed_sp=200)
    motor["C"].stop()

    motor_move("A", -80)

    # set initial position
    global current_a, current_b, current_c
    current_a = current_b = current_c = 0


def motor_move(idx, pos, speed=200):
    motor[idx].run_to_rel_pos(
        position_sp=pos,
        speed_sp=speed,
        stop_action='brake')
    motor_wait(idx)


def motor_wait(idx):
    motor[idx].wait_while("running")


def fold():
    global current_a
    motor_move("A", 80-current_a)
    current_a = 80


def unfold():
    global current_a
    motor_move("A", -current_a)
    current_a = 0


def up():
    global current_b
    if current_b > 50:
        motor_move("B", 50-current_b, 500)
        motor_move("B", -50, 100)
    else:
        motor_move("B", -current_b, 100)
    current_b = 0


def middle():
    global current_b
    motor_move("B", 300-current_b, 500)
    current_b = 300


def down():
    global current_b
    motor_move("B", 400-current_b, 500)
    current_b = 400


def goto(area):
    global current_a
    pos = -320 * area - current_a
    motor_move("C", pos)
    current_a = -320 * area


""" functions for Crane Application """


def init():
    motor_init()


def dump(area):
    goto(area)
    down()
    fold()
    middle()
    goto(1)
    down()
    unfold()
    up()


def on_button_up(state):
    if not state:
        return
    dump(2)


def on_button_down(state):
    if not state:
        return
    dump(0)

init()
btn.on_up = on_button_up
btn.on_down = on_button_down

cs.mode = 'COL-REFLECT'
while True:
    btn.process()
    sleep(0.01)

# cs.mode = 'COL-COLOR'
# while True:
#     if cs.value == COLOR_YELLOW:
#         dump(0)
#     elif cs.value == COLOR_GREEN:
#         dump(2)
