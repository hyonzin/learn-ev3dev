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

    mL.run_forever(speed_sp=min(1000, us.value()))
    mR.run_forever(speed_sp=min(1000, us.value()))

