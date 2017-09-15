from ev3dev.ev3 import *

Leds.set(Leds.LEFT, trigger = 'timer')
Leds.set_color(Leds.LEFT, Leds.GREEN)

ts = TouchSensor()


Leds.set(Leds.LEFT, brightness_pct = 1, delay_on = 1000, delay_off = 2000)

while True:
    if ts.value() == 1:
        Leds.all_off()
        break
