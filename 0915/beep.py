from ev3dev.ev3 import *

#Sound.beep().wait()
#Sound.tone(500, 2000).wait()

Sound.tone([
    (3000,200,10), (800,200,100)
]).wait()

#Sound.play('sounds/dog_x.wav').wait()
Sound.play('sounds/rooster.wav').wait()
Sound.play('sounds/chicken_rooster2.wav').wait()
