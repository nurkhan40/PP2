print("-----------------------------------------------------")
print('Python Iterators')
print("-----------------------------------------------------")



print('Example 1: Iterating through a tuple using an iterator')

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("-----------------------------------------------------")
print('Example 2: Iterating through a string using an iterator')

mystr = "banana"
myit1 = iter(mystr)

print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))

print("-----------------------------------------------------")
print('Example 3: Iterating through a tuple using a for loop')

mytuple1 = ("apple", "banana", "cherry")

for x in mytuple1:
	print(x)

print("-----------------------------------------------------")
print('Example 4: Iterating through a string using a for loop')

mystr1 = "banana"

for x in mystr1:
	print(x)

print("-----------------------------------------------------")
print('Example 5: Creating an iterable class without a stopping condition')

class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		x = self.a
		self.a += 1
		return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("-----------------------------------------------------")
print('Example 6: Creating an iterable class with a stopping condition')

class MyNumbers:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
	print(x)

print("-----------------------------------------------------")
