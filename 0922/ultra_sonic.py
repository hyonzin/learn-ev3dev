from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

us = UltrasonicSensor()
assert us.connected, "Connect a single US sonsor to any sensor port"
ts = TouchSensor(); assert ts.connected, "Connect a touch sensor to any port"

us.mode='US-DIST-CM'
units = us.units
e = 1

while not ts.value():
    distance = us.value()/10
    print(str(distance) + " " + units)

    if distance < 10 - e:
        Leds.set_color(Leds.LEFT, Leds.RED)
        mL.run_forever(speed_sp=-100)
        mR.run_forever(speed_sp=-100)
    elif distance > 10 + e:
        Leds.set_color(Leds.LEFT, Leds.YELLOW)
        mL.run_forever(speed_sp=100)
        mR.run_forever(speed_sp=100)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        mL.stop(stop_action="hold")
        mR.stop(stop_action="hold")

Sound.beep()
Leds.set_color(Leds.LEFT, Leds.GREEN)
mL.stop(stop_action="hold")
mR.stop(stop_action="hold")
