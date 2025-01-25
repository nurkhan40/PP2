"""
Python - Slicing Strings
"""

print("The code data type 'Slicing'\n")
print("You can return a range of characters by using the slice syntax.\n")
print("Specify the start index and the end index, separated by a colon, to return a part of the string.\n")
print("Example for Slicing:\n")
print('Get the characters from position 2 to position 5 (not included):\n')
print('b = "Hello, World!"\n')
print('print(b[2:5])\n')
print("The output\n")

# Slicing example:
b = "Hello, World!"
print(b[2:5])

print("----------------------------------------------------------------------------------------")

print("The code data type 'Slice From the Start'\n")
print("By leaving out the start index, the range will start at the first character.\n")
print("Example for Slice From the Start:\n")
print('Get the characters from the start to position 5 (not included):\n')
print('b = "Hello, World!"\n')
print('print(b[:5])\n')
print("The output\n")

# Slice from the start example:
b = "Hello, World!"
print(b[:5])

print("----------------------------------------------------------------------------------------")

print("The code data type 'Slice To the End'\n")
print("By leaving out the end index, the range will go to the end.\n")
print("Example for Slice To the End:\n")
print('Get the characters from position 2, and all the way to the end:\n')
print('b = "Hello, World!"\n')
print('print(b[2:])\n')
print("The output\n")

# Slice to the end example:
b = "Hello, World!"
print(b[2:])

print("----------------------------------------------------------------------------------------")

print("The code data type 'Negative Indexing'\n")
print("Use negative indexes to start the slice from the end of the string.\n")
print("Example for Negative Indexing:\n")
print('Get the characters:\n')
print('From: "o" in "World!" (position -5)\n')
print('To, but not included: "d" in "World!" (position -2):\n')
print('b = "Hello, World!"\n')
print('print(b[-5:-2])\n')
print("The output\n")

# Negative indexing example:
b = "Hello, World!"
print(b[-5:-2])

print("----------------------------------------------------------------------------------------")