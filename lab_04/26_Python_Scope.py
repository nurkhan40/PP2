"""
Python Scope
"""
"""
#-----------------------------------------------------
def myfunc():
  x = 300
  print(x)

myfunc()
#-----------------------------------------------------
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
#-----------------------------------------------------
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
#-----------------------------------------------------
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
#-----------------------------------------------------
def myfunc():
  global x
  x = 300

myfunc()

print(x)
#-----------------------------------------------------
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
#-----------------------------------------------------
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
#-----------------------------------------------------
"""
print("----------------------------------------------------------------------------------------")
print('Python Scope')

print("----------------------------------------------------------------------------------------")
print('Example 1: Local Scope')

def myfunc():
			x = 300
			print(x)

print('def myfunc():')
print('    x = 300')
print('    print(x)')
myfunc()

print("----------------------------------------------------------------------------------------")
print('Example 2: Function Inside Function')

def myfunc():
			x = 300
			def myinnerfunc():
						print(x)
			myinnerfunc()

print('def myfunc():')
print('    x = 300')
print('    def myinnerfunc():')
print('        print(x)')
print('    myinnerfunc()')
myfunc()

print("----------------------------------------------------------------------------------------")
print('Example 3: Global Scope')

x = 300

def myfunc():
			print(x)

print('x = 300')
print('def myfunc():')
print('    print(x)')
myfunc()
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 4: Local Scope with Same Variable Name')

x = 300

def myfunc():
			x = 200
			print(x)

print('x = 300')
print('def myfunc():')
print('    x = 200')
print('    print(x)')
myfunc()
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 5: Using the global Keyword')

def myfunc():
			global x
			x = 300

print('def myfunc():')
print('    global x')
print('    x = 300')
myfunc()
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 6: Changing Global Variable Inside Function')

x = 300

def myfunc():
			global x
			x = 200

print('x = 300')
print('def myfunc():')
print('    global x')
print('    x = 200')
myfunc()
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 7: nonlocal Keyword')

def myfunc1():
			x = "Jane"
			def myfunc2():
						nonlocal x
						x = "hello"
			myfunc2()
			return x

print('def myfunc1():')
print('    x = "Jane"')
print('    def myfunc2():')
print('        nonlocal x')
print('        x = "hello"')
print('    myfunc2()')
print('    return x')
print('print(myfunc1())')
print(myfunc1())

print("----------------------------------------------------------------------------------------")
