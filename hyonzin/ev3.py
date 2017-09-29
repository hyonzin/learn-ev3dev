#!/usr/bin/env python3

from ev3dev.ev3 import *
import ev3dev.fonts as fonts

class Ev3:
    def __init__(self):
        self.mL = LargeMotor('outC')
        self.mR = LargeMotor('outB')
        self.lcd = Screen()

        self.gy = GyroSensor()
        self.gy.mode = 'GYRO-ANG'
        assert self.gy.connected, "Connect a single gyro sensor to any sensor port"
        self.ts = TouchSensor()
        assert self.ts.connected, "Connect a touch sensor to any port"

    def rotate(self, degree, speed_sp=50):
        if degree > 0 :
            self.mL.run_forever(speed_sp= speed_sp)
            self.mR.run_forever(speed_sp=-speed_sp)
        else :
            self.mL.run_forever(speed_sp=-speed_sp)
            self.mR.run_forever(speed_sp= speed_sp)

        start_angle = current_angle = self.gy.value()
        finish_angle = start_angle + 180;

        while (degree > 0 and current_angle < finish_angle)\
                or (degree < 0 and current_angle > finish_angle):
            current_angle = self.gy.value()
            print(str(current_angle) + " " + self.gy.units)

        self.mL.stop(stop_action="hold")
        self.mR.stop(stop_action="hold")

    def go(self, position_sp, speed_sp=200):
        self.mL.run_to_rel_pos(position_sp=position_sp, speed_sp=speed_sp, stop_action='hold')
        self.mR.run_to_rel_pos(position_sp=position_sp, speed_sp=speed_sp, stop_action='hold')

    def show_text(self, text, font='luBS18'):
        self.lcd.clear()
        self.lcd.draw.text((60,60), text, font = fonts.load(font))
        self.lcd.update()
