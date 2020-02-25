from gpiozero import DigitalInputDevice

class encoder(object):
   def __init__(self,pin):
	self._value = 0
	encoder = DigitalInputDevice(pin)
	encoder.when_activated = self._increment
	encoder.when_deactivated = self._increment
   
   def reset(self):
	self._value = 0
   
   def _increment(self):
	self._value += 1

   def value(self):
	return self._value


enc = encoder(17)
while True:
	print('N = {}\r'.format(enc.value()))
