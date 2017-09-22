from ev3dev.ev3 import *

us = UltrasonicSensor()
assert us.connected, "Connect a single US sonsor to any sensor port"
ts = TouchSensor(); assert ts.connected, "Connect a touch sensor to any port"

us.mode='US-DIST-CM'
units = us.units

while not ts.value():
    distance = us.value()/10
    print(str(distance) + " " + units)

    if distance < 60:
        Leds.set_color(Leds.LEFT, Leds.RED)
    else:
        Leds.set_color(Leds.LEFT, Leds.RED)

Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)
