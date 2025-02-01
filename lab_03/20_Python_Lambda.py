"""
Python Lambda
"""
#-----------------------------------------------------
x = lambda a : a + 10
print(x(5))
#-----------------------------------------------------
x1 = lambda a, b : a * b
print(x1(5, 6))
#-----------------------------------------------------
x2 = lambda a, b, c : a + b + c
print(x2(5, 6, 2))
#-----------------------------------------------------
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#-----------------------------------------------------
def myfunc1(n):
  return lambda a : a * n

mytripler = myfunc1(3)

print(mytripler(11))
#-----------------------------------------------------
def myfunc2(n):
  return lambda a : a * n

mydoubler1 = myfunc2(2)
mytripler1 = myfunc2(3)

print(mydoubler1(11))
print(mytripler1(11))
#-----------------------------------------------------