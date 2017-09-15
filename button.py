from ev3dev.ev3 import *
from time import sleep

btn = Button()

def left(state):
    if state:
        print('Left button pressed')
    else:
        print('Left button released')

def right(state):
    print('Right button pressed' if state else 'Right button released')
def up(state):
    print('Up button pressed' if state else 'Up button released')
def down(state):
    print('Down button pressed' if state else 'Down button released')
def enter(state):
    print('Enter button pressed' if state else 'Enter button released')
def backspace(state):
    print('Backspace button pressed' if state else 'Backspace button released')

btn.on_left = left
btn.on_right = right
btn.on_up = up
btn.on_down = down
btn.on_enter = enter
btn.on_backspace = backspace

while True:
    btn.process()
    sleep(0.01)
