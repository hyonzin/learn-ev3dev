from ev3dev.ev3 import *
import time

ts = TouchSensor()
sec = 0

while True:
    if ts.value() == 1:
        Leds.all_off()
        break

    if sec == 0:
        Leds.set_color(Leds.LEFT, Leds.GREEN, pct=0)
        Leds.set_color(Leds.RIGHT, Leds.RED)

    elif sec == 10:
        Leds.set_color(Leds.LEFT, Leds.YELLOW)
        Leds.set_color(Leds.RIGHT, Leds.YELLOW)

    elif sec == 12:
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        Leds.set_color(Leds.RIGHT, Leds.YELLOW, pct=0)

    time.sleep(1)
    sec += 1
    if sec >= 22:
        sec = 0

