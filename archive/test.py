
'''----------------------------------------------
	Introduction to Objects
----------------------------------------------'''


class Parrot:
   
   # Class attributes
   species = "bird"

   # Instance attributes
   def __init__(self, name, age):
	self.name = name
	self.age = age

def testOne():
	# instantiate the Parrot class
	blu = Parrot("Blu", 10)
	woo = Parrot("Woo", 15)
	
	# access the class attributes
	print("Blu is a {}".format(blu.__class__.species))
	print("Woo is also a {}".format(blu.__class__.species))
	
	# access the instance attributes
	print("{} is {} years old".format(blu.name, blu.age))
	print("{} is {} years old".format(woo.name, woo.age))

'''----------------------------------------------
	Methods
----------------------------------------------'''

class Parrot:
   

   # Instance attributes
   def __init__(self, name, age):
	self.name = name
	self.age = age

   # Instance method
   def sing(self, song):
	return "{} sings {}".format(self.name, song)

   def dance(self):
	return "{} is now dancing".format(self.name)

# instantiate the object
green = Parrot("Green", 13)

# call our instance methods
print(green.sing("'Happy'"))
print(green.dance())
