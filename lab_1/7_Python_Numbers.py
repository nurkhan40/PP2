"""
Python Numbers
There are three numeric types in Python:
        int
        float
        complex
Variables of numeric types are created when you assign a value to them
See more in 8 Examples
"""

print("------------------------------------------")
print("Enter the number of example: ")
print("Enter 'q' to leave")
print("------------------------------------------")

while True:
    a = input()

    if a == "1":
        print("------------------------------------------")
        print("The code data types 'int', 'float', 'complex'\n")
        print('x = 1  # int\n')
        print('y = 2.8  # float\n')
        print('z = 1j  # complex\n')
        print("\n# display x, y, z and their data types:\nprint(x)\nprint(type(x))\nprint(y)\nprint(type(y))\nprint(z)\nprint(type(z))\n")
        print("The output\n")
        x = 1  # int
        y = 2.8  # float
        z = 1j   # complex
        print(x)
        print(type(x))
        print(y)
        print(type(y))
        print(z)
        print(type(z))
        print("------------------------------------------")
    elif a == "2":
        print("------------------------------------------")
        print("The code data type 'int' (Integer)\n")
        print("Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.\n")
        print("Example\n")
        print("Integers:\n")
        print('x = 1\n')
        print('y = 35656222554887711\n')
        print('z = -3255522\n')
        print("\n# display x, y, z and their data types:\nprint(type(x))\nprint(type(y))\nprint(type(z))\n")
        print("The output\n")
        x = 1
        y = 35656222554887711
        z = -3255522
        print(type(x))
        print(type(y))
        print(type(z))
        print("------------------------------------------")
    elif a == "3":
        print("------------------------------------------")
        print("The code data type 'float' (Floating Point Number)\n")
        print("Float, or 'floating point number' is a number, positive or negative, containing one or more decimals.\n")
        print("Float can also be scientific numbers with an 'e' to indicate the power of 10.\n")
        print("Example\n")
        print("Floats:\n")
        print('x = 35e3\n')
        print('y = 12E4\n')
        print('z = -87.7e100\n')
        print("\n# display x, y, z and their data types:\nprint(type(x))\n\tprint(type(y))\nprint(type(z))\n")
        print("The output\n")
        x = 35e3
        y = 12E4
        z = -87.7e100
        print(type(x))
        print(type(y))
        print(type(z))
        print("------------------------------------------")
    elif a == "4":
        print("------------------------------------------")
        print("The code data type 'complex' (Complex Number)\n")
        print("Complex numbers are written with a 'j' as the imaginary part:\n")
        print("Example\n")
        print("Complex:\n")
        print('x = 3+5j\n')
        print('y = 5j\n')
        print('z = -5j\n')
        print("\n# display x, y, z and their data types:\nprint(type(x))\n\tprint(type(y))\nprint(type(z))\n")
        print("The output\n")
        x = 3 + 5j
        y = 5j
        z = -5j
        print(type(x))
        print(type(y))
        print(type(z))
        print("------------------------------------------")
    elif a == "5":
        print("------------------------------------------")
        print("The code data type 'Type Conversion'\n")
        print("You can convert from one type to another with the int(), float(), and complex() methods:\n")
        print("Example\n")
        print("Convert from one type to another:\n")
        print('x = 1    # int\n')
        print('y = 2.8  # float\n')
        print('z = 1j   # complex\n')
        print("\n# convert from int to float:\na = float(x)\n")
        print("# convert from float to int:\nb = int(y)\n")
        print("# convert from int to complex:\n\tc = complex(x)\n")
        print("\n# display the converted values:\nprint(a)\nprint(b)\nprint(c)\n")
        print("\n# display the types of the converted values:\nprint(type(a))\nprint(type(b))\nprint(type(c))\n")
        print("The output\n")
        x = 1    # int
        y = 2.8  # float
        z = 1j   # complex

        #convert from int to float:
        a = float(x)

        #convert from float to int:
        b = int(y)

        #convert from int to complex:
        c = complex(x)

        print(a)
        print(b)
        print(c)

        print(type(a))
        print(type(b))
        print(type(c))
        print("------------------------------------------")
    elif a == "6":
        print("------------------------------------------")
        print("The code data type 'Random Number'\n")
        print("Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:\n")
        print("Example\n")
        print("Import the random module, and display a random number between 1 and 9:\n")
        print('import random\n')
        print('print(random.randrange(1, 10))\n')
        print("The output\n")
        import random
        print(random.randrange(1, 10))
        print("------------------------------------------")
    elif a == 'q':
        print("See you next time!")
        break
    else:
        print(" ")
        print("Eneter number between 1-4!")