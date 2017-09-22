from ev3dev.ev3 import *

mL = LargeMotor('outC')
mR = LargeMotor('outB')

us = UltrasonicSensor()
assert us.connected, "Connect a single US sonsor to any sensor port"
ts = TouchSensor(); assert ts.connected, "Connect a touch sensor to any port"

us.mode='US-DIST-CM'
units = us.units

m_speed = 1500
e = 50 # (mm)

while not ts.value():
    distance = us.value()/10
    print(str(distance) + " " + units)

    mL.run_forever(speed_sp=min(m_speed, max(us.value() - e, 0)))
    mR.run_forever(speed_sp=min(m_speed, max(us.value() - e, 0)))

