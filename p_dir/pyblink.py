import time
import pyb
green = 2
yellow = 3
while True:
    pyb.LED(green).on()
    pyb.LED(yellow).on()
    time.sleep(1)
    pyb.LED(green).off()
    pyb.LED(yellow).off()
    time.sleep(1)

