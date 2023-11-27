import pyb
green = 2
yellow = 3
while True:
    pyb.LED(green).on()
    pyb.LED(yellow).on()
    pyb.delay(1000)
    pyb.LED(green).off()
    pyb.LED(yellow).off()
    pyb.delay(1000)

