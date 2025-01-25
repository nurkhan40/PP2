"""
Python Variables.

Variables.

Variables are containers for storing data values.

Creating Variables

Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.

There are Exmaple 1 and 2!
"""


"""
Casting.

If you want to specify the data type of a variable, 
this can be done with casting.

Get the Type.

You can get the data type of a variable with the type() function.

There are Exmaple 3 and 4!
"""


"""
Single or Double Quotes?

String variables can be declared either by using 
single or double quotes.

Case-Sensitive.

Variable names are case-sensitive.

There are Exmaple 5 and 6!
"""

print("Enter the number of example: ")
print("Enter 'q' to leave")

while True:
    a = input()

    if a == "1":
        print(" ")
        print("The code")
        print("x = 5")
        print('y ="John"')
        print("print(x)")
        print("print(y)")
        print(" ")
        print("The answer: ")
        x = 5
        y = "John"
        print(x)
        print(y)
        print(" ")
    elif a == "2":
        print(" ")
        print("Variables do not need to be declared with any particular type, and can even change type after they have been set.")
        print("The code:")
        print("x = 4")
        print('x ="Sally"')
        print("print(x)")
        print(" ")
        print("The answer: ")
        x = 4
        x = "Sally"
        print(x)
        print(" ")
        print("We can see that x used last mentioned variable!")
        print(" ")
    elif a == "3":
        print(" ")
        print("Casting")
        print("The code: ")
        print("x = str(3)    # x will be 3")
        print("y = int(3)    # y will be 3")
        print("z = float(3)  # z will be 3.0")
        print(" ")
        print("The answer: ")
        x = str(3)    # x will be '3'
        y = int(3)    # y will be 3
        z = float(3)  # z will be 3.0
        print(x)
        print(y)
        print(x)
        print(" ")
    elif a == "4":
        print(" ")
        print("Get the Type")
        print("The code: ")
        print("x = 5")
        print('y = "John"')
        print("print(type(x))")
        print("print(type(y))")
        print(" ")
        print("The answer: ")
        x = 5
        y = "John"
        print(type(x))
        print(type(y))
        print(" ")
        print("We can get the data type of a variable with the type() function.")
        print(" ")
    elif a == "6":
        print(" ")
        print("Case-Sensetive")
        print("The code: ")
        print("a = 4")
        print('A = "Sally"')
        print("#A will nor overwrite a")
        print(" ")
        print("The answer: ")
        a = 4
        A = "Sally"
        print(a)
        print(A)
        print(" ")
    elif a == "5":
        print(" ")
        print("Single or Double Quotes?")
        print("The code: ")
        print('x = "John"')
        print("# is the same as")
        print("x = 'John'")
        print(" ")
        print("The answer: ")
        x = "John"
        x = 'John'
        print(x)
        print("String variables can be declared either by using single or double quotes")
        print(" ")
    elif a == "q":
        print("Thank you! See you next time!")
        break
    else:
        print(" ")
        print("Eneter number between 1-6!")
        print(" ")