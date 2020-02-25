from gpiozero import DigitalInputDevice

class hallSensor(object):
   def __init__(self,pin1, pin2, pin3):
	self._value = 0
	hallSensor = DigitalInputDevice(pin)
	encoder.when_actvated