"""
Python - Global Variables

Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

"""

print("Enter the number of example: ")
print("Enter 'q' to leave")

while True:
    a = input()

    if a == "1":
        print(" ")
        print("Create a variable outside of a function, and use it inside the function")
        print("The code:")
        print('x = "awesome"')
        print("def myfunc():")
        print('  print("Python is " + x)')
        print("myfunc()")
        print(" ")
        print("The answer: ")
        x = "awesome"

        def myfunc():
            print("Python is " + x)

        myfunc()
        print(" ")
    elif a == "2":
        print(" ")
        print("If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.")
        print("Create a variable inside a function, with the same name as the global variable")
        print("The code:")
        print('x = "awesome"')
        print(" ")
        print("def myfunc():")
        print('    x = "fantastic"')
        print('    print("Python is " + x)')
        print(" ")
        print("myfunc()")
        print(" ")
        print('print("Python is " + x)')
        print(" ")
        print("The answer: ")
        x = "awesome"

        def myfunc():
            x = "fantastic"
            print("Python is " + x)

        myfunc()

        print("Python is " + x)
        print(" ")
    elif a == "3":
        print(" ")
        print("The global Keyword")
        print(" ")
        print("Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.")
        print("To create a global variable inside a function, you can use the global keyword.")
        print("If you use the global keyword, the variable belongs to the global scope:")
        print(" ")
        print("The code:")
        print("def myfunc():")
        print("  global x")
        print('  x = "fantastic"')
        print(" ")
        print("myfunc()")
        print(" ")
        print('print("Python is " + x)')
        print(" ")
        print("The answer is: ")
        def myfunc():
            global x
            x = "fantastic"

        myfunc()

        print("Python is " + x)
        print(" ")
    elif a == "4":
        print(" ")
        print("Also, use the global keyword if you want to change a global variable inside a function.")
        print("To change the value of a global variable inside a function, refer to the variable by using the global keyword:")
        print("The code:")
        print(" ")
        print('x = "awesome"')
        print(" ")
        print("def myfunc():")
        print('  global x\n  x = "fantastic"\n\nmyfunc()\n\nprint("Python is " + x)')
        x = "awesome"

        def myfunc():
            global x
            x = "fantastic"

        myfunc()

        print("\nThe answer is")
        print("Python is " + x)
        print(" ")
    elif a == 'q':
        print("See you next time!")
        break
    else:
        print(" ")
        print("Eneter number between 1-4!")
        print(" ")
