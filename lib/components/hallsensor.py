from gpiozero import DigitalInputDevice

class HallSensor(object):
"""
	HallSensor Class
	----------------

	Data structure that represents the state of three GPIO input pins corresponding to inputs from three individual hall sensor components

	Functional Description
	- continuously monitors state of pin
	- prints value as a 3-tuple
	- determines phase given inputs

	# Class Attributes

	# instance Attributes

	# Instance Methods

	-------------------------
	Notes:

	DigitalInputDevice API
	- wait_for_active
	- wait_for_inactive
	- active_time
	- inactive_time
	- value
	- when_activated
	- when_deactivated


"""
	def __init__(self, pin1, pin2, pin3):
		hall1 = DigitalInputDevice(pin1)
		hall2 = DigitalInputDevice(pin2)
		hall3 = DigitalInputDevice(pin3)

		self._hall_1_value = hall1.value

		hall1.when_activated   = self.
		hall1.when_deactivated

		hall2.when_activated
		hall2.when_deactivated

		hall3.when_activated
		hall3.when_deactivated

	def
