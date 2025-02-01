"""
Python Polymorphism
"""
"""
#-----------------------------------------------------
x = "Hello World!"

print(len(x))
#-----------------------------------------------------
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))
#-----------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
#-----------------------------------------------------
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
#-----------------------------------------------------
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
#-----------------------------------------------------
"""

print("----------------------------------------------------------------------------------------")
print('Python Polymorphism')

print("----------------------------------------------------------------------------------------")
print('Example 1: Using len() function on different data types')

print("----------------------------------------------------------------------------------------")
print('print(len("Hello World!"))')
print(len("Hello World!"))

print("----------------------------------------------------------------------------------------")
print('print(len(("apple", "banana", "cherry")))')
print(len(("apple", "banana", "cherry")))

print("----------------------------------------------------------------------------------------")
print('thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}')
print('print(len(thisdict))')
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(len(thisdict))

print("----------------------------------------------------------------------------------------")
print('Example 2: Polymorphic behavior with different classes')

class Car:
			def __init__(self, brand, model):
						self.brand = brand
						self.model = model

			def move(self):
						print("Drive!")

class Boat:
			def __init__(self, brand, model):
						self.brand = brand
						self.model = model

			def move(self):
						print("Sail!")

class Plane:
			def __init__(self, brand, model):
						self.brand = brand
						self.model = model

			def move(self):
						print("Fly!")

car1 = Car("Ford", "Mustang")       # Create a Car object
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat object
plane1 = Plane("Boeing", "747")     # Create a Plane object

for x in (car1, boat1, plane1):
			print("----------------------------------------------------------------------------------------")
			print(f'print({x.__class__.__name__}.move())')
			x.move()

print("----------------------------------------------------------------------------------------")
print('Example 3: Inheritance-based polymorphism')

class Vehicle:
			def __init__(self, brand, model):
						self.brand = brand
						self.model = model

			def move(self):
						print("Move!")

class Car(Vehicle):
			pass

class Boat(Vehicle):
			def move(self):
						print("Sail!")

class Plane(Vehicle):
			def move(self):
						print("Fly!")

car1 = Car("Ford", "Mustang")       # Create a Car object
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat object
plane1 = Plane("Boeing", "747")     # Create a Plane object

for x in (car1, boat1, plane1):
			print("----------------------------------------------------------------------------------------")
			print(f'print({x.__class__.__name__}("{x.brand}", "{x.model}"))')
			print(x.brand)
			print(x.model)
			print(f'print({x.__class__.__name__}.move())')
			x.move()

print("----------------------------------------------------------------------------------------")
