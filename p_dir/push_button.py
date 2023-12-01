from pyb import Pin
pinX1 = Pin('X1', Pin.IN, Pin.PULL_UP)
pinX2 = Pin('X2', Pin.OUT_PP)
while True:
    if pinX1.value() == 0:
        pinX2.high()
    else:
        pinX2.low()

