import ev3dev.ev3 as ev3
ts = ev3.TouchSensor()

while True:
    if (ts.is_pressed):
        print("hi")
