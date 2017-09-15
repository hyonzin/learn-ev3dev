#!/usr/bin/env python3

import ev3dev.ev3 as ev3
ts = ev3.TouchSensor()

while True:
    if ts.value()==1:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    else:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)

