"""
Python Variables - Assign Multiple Values

Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line

One Value to Multiple Variables
And you can assign the same value to multiple variables in one line

Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""

print("Enter the number of example: ")
print("Enter 'q' to leave")

while True:
    a = input()

    if a == "1":
        print(" ")
        print("Many Values to Multiple Variables")
        print("Python allows you to assign values to multiple variables in one line")
        print('x, y, z = "Orange", "Banana", "Cherry"')
        print("print(x)")
        print("print(y)")
        print("print(z)")
        print(" ")
        print("The answer: ")
        x, y, z = "Orange", "Banana", "Cherry"
        print(x)
        print(y)
        print(z)
        print(" ")
        print("Note: Make sure the number of variables matches the number of values, or else you will get an error.")
        print(" ")
    elif a == "2":
        print(" ")
        print("One Value to Multiple Variables")
        print("And you can assign the same value to multiple variables in one line:")
        print('x = y = z = "Orange"')
        print("print(x)")
        print("print(y)")
        print("print(z)")
        print(" ")
        print("The answer: ")
        x = y = z = "Orange"
        print(x)
        print(y)
        print(z)
        print(" ")
    elif a == "3":
        print(" ")
        print("Unpack a Collection")
        print("If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.")
        print("Unpack a list:")
        print('fruits = ["apple", "banana", "cherry"]')
        print("x, y, z = fruits")
        print("print(x)")
        print("print(y)")
        print("print(z)")
        print(" ")
        print("The answer: ")
        fruits = ["apple", "banana", "cherry"]
        x, y, z = fruits
        print(x)
        print(y)
        print(z)
        print(" ")
    elif a == 'q':
        print("See you next time!")
        break
    else:
        print(" ")
        print("Eneter number between 1-4!")
        print(" ")