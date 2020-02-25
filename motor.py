from gpiozero import DigitalInputDevice, DigitalOutputDevice

class Motor(object)

	def __init__(self,
   		         pin_hall_1,
		         pin_hall_2,
		         pin_hall_3,
		         pin_encoder,
		         pin_phase_1,
		         pin_phase_2,
		         pin_phase_3,):
		# Inputs
		hall_1 = DigitalInputDevice(pin_hall_1)
		hall_2 = DigitalInputDevice(pin_hall_2)
		hall_3 = DigitalInputDevice(pin_hall_3)

		encoder = DigitalInputDevice(pin_encoder)

		# Outputs
		phase_1 = DigitalOutputDevice(pin_phase_1)
		phase_2 = DigitalOutputDevice(pin_phase_2)
		phase_3 = DigitalOutputDevice(pin_phase_2)

		# Event Handling - Inputs only
		hall_1.when_activated   = 
		hall_1.when_deactivated = 

	# Input methods


	# Output methods



