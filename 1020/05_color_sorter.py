#!/usr/bin/env python3

from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep

lcd = Screen()
ts = TouchSensor()
cs = ColorSensor()
motor_m = MediumMotor('outA')
motor_l = LargeMotor('outD')

cs.mode = 'COL-COLOR'
COLORS = ['unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown']

pos_interval = 190

""" functions for LCD """

def lcd_show(str):
    lcd.clear()
    lcd.draw.text((60,60), str, font = fonts.load('luBS24'))
    lcd.update()


""" functions for motor """

def motor_m_push():
    motor_m.run_timed(time_sp=1500, speed_sp=-100)
    sleep(1.5)

def motor_m_pull():
    motor_m.run_timed(time_sp=1500, speed_sp=100)
    sleep(1.5)

def motor_l_init():
    motor_l.run_forever(speed_sp=-200)
    while not ts.is_pressed:
        sleep(0.1)
    motor_l.stop(stop_action="brake")
    motor_l.reset()

def motor_l_go(pos):
    if pos != 0:
        motor_l.run_to_rel_pos(position_sp=pos, speed_sp=300, stop_action='brake')
        motor_l.wait_while('running')

""" functions for color sensor """





""" functions for Color Sorter Application """

def init():
    motor_l_init()
    motor_m_pull()

def sort(value):
    global prev_value
    motor_l_go(pos_interval * (value - prev_value))
    motor_m_push()
    motor_m_pull()

global prev_value
prev_value=2

init()
while True:
    sleep(0.5)
    cs_value = cs.value()
    lcd_show(COLORS[cs_value])
    if cs_value >= 2 and cs_value <= 5 :
        sort(cs_value)
        prev_value = cs_value

