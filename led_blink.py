from ev3dev.ev3 import *

Leds.set(Leds.LEFT, trigger = 'timer')
Leds.set(Leds.LEFT, brightness_pct = 1, delay_off = 100)
Leds.set_color(Leds.LEFT, Leds.GREEN)

ts = TouchSensor()

while True:
    if ts.value() == 1:
        Leds.all_off()
        break
