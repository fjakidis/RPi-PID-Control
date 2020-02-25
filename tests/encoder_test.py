from gpiozero import DigitalInputDevice
from signal import pause
import time

class encoder(object):
   def __init__(self):
      self.value = 0
   
   def reset(self):
      self.value = 0
   
   def increment(self):
      self.value += 1


def activated()   : my_enc.increment()  
def deactivated() : return 0

my_enc = encoder()

enc = DigitalInputDevice(17)
enc.when_activated = activated
enc.when_deactivated = deactivated

start = time.time()
while True:
   elapsed = time.time()-start 
   print('Time {0:0.2f} -- N = {1} -- Velocity {2}'.format(elapsed,my_enc.value,my_enc.value/elapsed),end="\r")


pause()