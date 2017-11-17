#!/usr/bin/env python3

from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from time import sleep

lcd = Screen()
btn = Button()

mL = LargeMotor("outA")
mR = LargeMotor("outB")
mH = MediumMotor("outC")


