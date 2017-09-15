from ev3dev.ev3 import *

#Leds.set(Leds.LEFT, trigger = 'timer')
#Leds.set(Leds.LEFT, brightness_pct = 1, delay_off = 100)
Leds.set_color(Leds.LEFT, Leds.GREEN)
Leds.set_color(Leds.RIGHT, Leds.RED)
Leds.set(Leds.LEFT, brightness_pct = 1, delay_off = 3000)
Leds.set(Leds.RIGHT, brightness_pct = 1, delay_on = 3000)

ts = TouchSensor()

while True:
    if ts.value() == 1:
        Leds.all_off()
        break
