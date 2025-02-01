"""
Python Modules
"""
"""
#-----------------------------------------------------
def greeting(name):
  print("Hello, " + name)
#-----------------------------------------------------
import mymodule

mymodule.greeting("Jonathan")
#-----------------------------------------------------
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#-----------------------------------------------------
import mymodule

a = mymodule.person1["age"]
print(a)
#-----------------------------------------------------
import mymodule as mx

a = mx.person1["age"]
print(a)
#-----------------------------------------------------
import platform

x = platform.system()
print(x)
#-----------------------------------------------------
import platform

x = dir(platform)
print(x)
#-----------------------------------------------------
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#-----------------------------------------------------
from mymodule import person1

print (person1["age"])
#-----------------------------------------------------
"""

print("----------------------------------------------------------------------------------------")
print('Python Modules')

print("----------------------------------------------------------------------------------------")
print('Example 1: Creating a Module')

def greeting(name):
			print("Hello, " + name)

print('def greeting(name):')
print('    print("Hello, " + name)')

print("----------------------------------------------------------------------------------------")
print('Example 2: Using a Module')

import mymodule

print('import mymodule')
print('mymodule.greeting("Jonathan")')
mymodule.greeting("Jonathan")

print("----------------------------------------------------------------------------------------")
print('Example 3: Dictionary in a Module')

person1 = {
			"name": "John",
			"age": 36,
			"country": "Norway"
}

print('person1 = {')
print('    "name": "John",')
print('    "age": 36,')
print('    "country": "Norway"')
print('}')

print("----------------------------------------------------------------------------------------")
print('Example 4: Importing Specific Dictionary Item')

import mymodule

print('import mymodule')
print('a = mymodule.person1["age"]')
a = mymodule.person1["age"]
print('print(a)')
print(a)

print("----------------------------------------------------------------------------------------")
print('Example 5: Renaming a Module')

import mymodule as mx

print('import mymodule as mx')
print('a = mx.person1["age"]')
a = mx.person1["age"]
print('print(a)')
print(a)

print("----------------------------------------------------------------------------------------")
print('Example 6: Using platform Module')

import platform

print('import platform')
print('x = platform.system()')
x = platform.system()
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 7: Defining Functions and Dictionaries in a Module')

def greeting(name):
			print("Hello, " + name)

person1 = {
			"name": "John",
			"age": 36,
			"country": "Norway"
}

print('def greeting(name):')
print('    print("Hello, " + name)')

print('person1 = {')
print('    "name": "John",')
print('    "age": 36,')
print('    "country": "Norway"')
print('}')

print("----------------------------------------------------------------------------------------")
print('Example 8: Importing Specific Data from a Module')

from mymodule import person1

print('from mymodule import person1')
print('print (person1["age"])')
print(person1["age"])

print("----------------------------------------------------------------------------------------")
