import pyb

green = 2
yellow = 3

def BlinkYellow():
	for x in range(0,4):
		pyb.LED(yellow),on()
		pyb.delay(1000)
		pyb.LED(yellow).off()
		pyb.delay(1000)

sw = pyb.Switch()
sw.callback(BlinkYellow)

while True:
	pyb.LED(green).on()
	pyb.delay(1000)
	pyb.LED(green).off()
	pyb.delay(1000)
