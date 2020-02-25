
'''----------------------------------------------
	Introduction to Objects
----------------------------------------------'''


class ParrotA:
   
   # Class attributes
   species = "bird"

   # Instance attributes
   def __init__(self, name, age):
      self.name = name
      self.age = age

# instantiate the Parrot class
blu = ParrotA("Blu", 10)
woo = ParrotA("Woo", 15)
	
# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(blu.__class__.species))
print('\n')
	
# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
print('\n')

'''----------------------------------------------
	Methods
----------------------------------------------'''

class ParrotB:
   

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
green = ParrotB("Green", 13)

# call our instance methods
print(green.sing("'Happy'"))
print(green.dance())
print('\n')

'''----------------------------------------------
	Inheritance
----------------------------------------------'''

# Parent Class
class Bird:

   def __init__(self):
      print("Bird is ready")

   def whoisThis(self):
      print("Bird")

   def swim(self):
      print("Swim faster")

# Child class
class PenguinB(Bird):

   def __init__(self):
      # call super() function (pull content of __init__() from the parent class into the child class)
      super().__init__()
      print("Penguin is ready")

   def whoisThis(self):
      print("Penguin")

   def run(self):
      print("Run faster")

peggy = PenguinB()
peggy.whoisThis()
peggy.swim()
peggy.run()
print('\n')

'''----------------------------------------------
	Encapsulation
----------------------------------------------'''

class Computer:

   def __init__(self):
      self.__maxprice = 900

   def sell(self):
      print("Selling Price: {}".format(self.__maxprice))

   def setMaxPrice(self, price):
      self.__maxprice = price

c = Computer()
c.sell()

# change price
c.setMaxPrice(1000)
c.sell()
print('\n')

'''----------------------------------------------
	Polymorphism
----------------------------------------------'''

class Parrot:

   def __init__(self):
      pass

   def fly(self):
      print("Parrot can fly")

   def swim(self):
      print("Parrot can't swim")

class Penguin:

   def __init__(self):
      pass

   def fly(self):
      print("Penguin can't fly")

   def swim(self):
      print("Penguin can swim")


# common interface
def flying_test(bird):
   bird.fly()

# instantiate objects

yellow = Parrot()
orange = Penguin()

# passing the object
flying_test(yellow)
flying_test(orange)
print('\n')















