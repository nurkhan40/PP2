"""
Python Functions
"""
#-----------------------------------------------------

def my_function():
  print("Hello from a function")

#-----------------------------------------------------

def my_function1():
  print("Hello from a function")

my_function1()

#-----------------------------------------------------

def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

#-----------------------------------------------------

def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes")

#-----------------------------------------------------

def my_function4(*kids):
  print("The youngest child is " + kids[2])

my_function4("Emil", "Tobias", "Linus")

#-----------------------------------------------------

def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)

my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#-----------------------------------------------------

def my_function6(**kid):
  print("His last name is " + kid["lname"])

my_function6(fname = "Tobias", lname = "Refsnes")

#-----------------------------------------------------

def my_function7(country = "Norway"):
  print("I am from " + country)

my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")

#-----------------------------------------------------

def my_function8(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function8(fruits)

#-----------------------------------------------------

def my_function9(x):
  return 5 * x

print(my_function9(3))
print(my_function9(5))
print(my_function9(9))

#-----------------------------------------------------

def myfunctionq():
  pass

#-----------------------------------------------------

def my_functionw(x, /):
  print(x)

my_function(3)

#-----------------------------------------------------

def my_functione(x):
  print(x)

my_functione(x = 3)

#-----------------------------------------------------

def my_functiona(*, x):
  print(x)

my_functiona(x = 3)

#-----------------------------------------------------

def my_functio(x):
  print(x)

my_functio(3)

#-----------------------------------------------------

def my_functionz(a, b, /, *, c, d):
  print(a + b + c + d)

my_functionz(5, 6, c = 7, d = 8)

#-----------------------------------------------------

def tri_recursionx(k):
  if(k > 0):
    result = k + tri_recursionx(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursionx(6)

#-----------------------------------------------------