import pyb, micropython

micropython.alloc_emergency_exception_buf(100)
green = 2
yellow = 3

class Blink(object):
	def __init__(self,timer,led):
		self.led = led
		timer.callback(self.cb)
	def cb(self,tim):
		self.led.toggle()
greenLED = Blink(pyb.Timer(4, freq=1), pyb.LED(green))
yellowLED = Blink(pyb.Timer(2, freq=2), pyb.LED(yellow))
