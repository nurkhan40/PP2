"""
Python - Output Variables

Output Variables
The Python print() function is often used to output variables.
See more in Examples 1-6!
"""

print("Enter the number of example: ")
print("Enter 'q' to leave")

while True:
    a = input()

    if a == "1":
        print(" ")
        print("The code:")
        print('x = "Python is awesome"')
        print("print(x)")
        print("The answer: ")
        x = "Python is awesome"
        print(x)
        print(" ")
    elif a == "2":
        print(" ")
        print("In the print() function, you output multiple variables, separated by a comma")
        print("The code:")
        print('x = "Python"')
        print('y = "is"')
        print('z = "awesome"')
        print("print(x, y, z)")
        print(" ")
        print("The answer: ")
        x = "Python"
        y = "is"
        z = "awesome"
        print(x, y, z)
        print(" ")
    elif a == "3":
        print(" ")
        print("You can also use the + operator to output multiple variables")
        print("The code:")
        print('x = "Python "')
        print('y = "is "')
        print('z = "awesome"')
        print("print(x + y + z)")
        print(" ")
        print("The answer: ")
        x = "Python "
        y = "is "
        z = "awesome"
        print(x + y + z)
        print('Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".')
        print(" ")
    elif a == "4":
        print(" ")
        print("For numbers, the + character works as a mathematical operator")
        print("The code:")
        print("x = 5")
        print("y = 10")
        print("print(x + y)")
        print(" ")
        print("The answer: ")
        x = 5
        y = 10
        print(x + y)
        print(" ")
    elif a == "5":
        print(" ")
        print("In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error")
        print("The code:")
        print("x = 5")
        print('y = "John"')
        print("print(x + y)")
        print(" ")
        print("The answer: ")
        print("Error!")
        print(" ")
    elif a == "6":
        print(" ")
        print("The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types")
        print("The code:")        
        print("x = 5")
        print('y = "John"')
        print("print(x, y)")
        print(" ")
        print("The answer: ")
        x = 5
        y = "John"
        print(x, y)
        print(" ")
    elif a == 'q':
        print("See you next time!")
        break
    else:
        print(" ")
        print("Eneter number between 1-6!")
        print(" ")
