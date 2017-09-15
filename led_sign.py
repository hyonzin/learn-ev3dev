from ev3dev.ev3 import *
import time

ts = TouchSensor()
sec = 0

while True:
    if ts.value() == 1:
        Leds.all_off()
        break

    if sec == 0:
        Leds.set(Leds.LEFT, brightness_pct = 0)

        Leds.set_color(Leds.RIGHT, Leds.RED)
        Leds.set(Leds.RIGHT, brightness_pct = 1)

    elif sec == 10:
        Leds.set_color(Leds.LEFT, Leds.YELLOW)
        Leds.set(Leds.LEFT, brightness_pct = 1)

        Leds.set(Leds.RIGHT, brightness_pct = 0)
        Leds.set_color(Leds.RIGHT, Leds.YELLOW)
        Leds.set(Leds.RIGHT, brightness_pct = 1)
    elif sec == 12:
        Leds.set(Leds.LEFT, brightness_pct = 0)
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        Leds.set(Leds.LEFT, brightness_pct = 1)

        Leds.set(Leds.RIGHT, brightness_pct = 0)

    time.sleep(1)
    sec += 1
    if sec >= 22:
        sec = 0

