import gpiozero as gp
import curses 
import time

out1 = gp.DigitalOutputDevice(16)		# board pin 36
out2 = gp.DigitalOutputDevice(20)		# board pin 38
out3 = gp.DigitalOutputDevice(21)		# board pin 40


# Want:
# - Output signals modelling hall-sensor phase

t = 0.05

class HallTest:
	def __init__(self):
		pass

	def a000(self):
		out1.off()
		out2.off()
		out3.off()
		print('000')

	def a001(self):
		out1.off()
		out2.off()
		out3.on()
		print('001')
	
	def a010(self):
		out1.off()
		out2.on()
		out3.off()
		print('010')
	
	def a011(self):
		out1.off()
		out2.on()
		out3.on()
		print('011')
	
	def a100(self):
		out1.on()
		out2.off()
		out3.off()
		print('100')
	
	def a101(self):
		out1.on()
		out2.off()
		out3.on()
		print('101')

	def a110(self):
		out1.on()
		out2.on()
		out3.off()
		print('110')

	def a111(self):
		out1.on()
		out2.on()
		out3.on()
		print('111')

	def forward1(self):
		'''
		Forward
		-------

		A - 110
		B - 011
		C - 101
		'''
		self.a110()
		time.sleep(t)
		self.a011()
		time.sleep(t)
		self.a101()
		time.sleep(t)

	def forward2(self):
		'''
		Forward
		-------

		A - 010
		B - 001
		C - 100
		'''
		self.a010()
		time.sleep(t)
		self.a001()
		time.sleep(t)
		self.a100()
		time.sleep(t)

	def backward1(self):
		'''
		Backward
		-------

		C - 101
		B - 011
		A - 110
		'''
		self.a101()
		time.sleep(t)
		self.a011()
		time.sleep(t)
		self.a110()
		time.sleep(t)

	def backward2(self):
		'''
		Backward
		-------

		C - 100
		B - 001
		A - 010
		'''
		self.a100()
		time.sleep(t)
		self.a001()
		time.sleep(t)
		self.a010()
		time.sleep(t)


test = HallTest()

while True:
	test.forward1()
	#test.forward2()
	#test.backward1()
	#test.backward2()
	print('-------')

# Want:
# - Output signals modelling encoder

