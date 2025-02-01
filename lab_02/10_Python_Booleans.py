"""
Python Booleans
Booleans represent one of two values: True or False.
"""
print("Enter the number of example: ")
print("Enter 'q' to leave")

while True:
    a = input()
    if a == "1":
        print("----------------------------------------------------------------------------------------")
        print("Boolean Values")
        print("In programming you often need to know if an expression is True or False.\n")
        print("You can evaluate any expression in Python, and get one of two answers, True or False.\n")
        print("When you compare two values, the expression is evaluated and Python returns the Boolean answer:\n")
        print("ExampleGet your own Python Server")

        print("----------------------------------------------------------------------------------------")
        print('print(10 > 9)')
        print(10 > 9)

        print("----------------------------------------------------------------------------------------")
        print('print(10 == 9)')
        print(10 == 9)

        print("----------------------------------------------------------------------------------------")
        print('print(10 < 9)')
        print(10 < 9)

        print("----------------------------------------------------------------------------------------")
        print("It was a 1 Example! Type number of next Example: ")
    elif a == "2":
        print("----------------------------------------------------------------------------------------")
        print("Example")
        print("Print a message based on whether the condition is True or False:\n")

        print("----------------------------------------------------------------------------------------")
        print("a = 200")
        print("b = 33\n")

        print("if b > a:")
        print("  print(\"b is greater than a\")")
        print("else:")
        print("  print(\"b is not greater than a\")\n")

        a = 200
        b = 33

        if b > a:
            print("b is greater than a")
        else:
            print("b is not greater than a")

        print("----------------------------------------------------------------------------------------")
        print("It was a 2 Example! Type number of next Example: ")
    elif a == "3":
        print("----------------------------------------------------------------------------------------")
        print("Evaluate Values and Variables")
        print("The bool() function allows you to evaluate any value, and give you True or False in return,\n")

        print("----------------------------------------------------------------------------------------")
        print("Example")
        print("Evaluate a string and a number:\n")

        print("----------------------------------------------------------------------------------------")
        print('print(bool("Hello"))')
        print(bool("Hello"))

        print("----------------------------------------------------------------------------------------")
        print("print(bool(15))")
        print(bool(15))

        print("----------------------------------------------------------------------------------------")
        print("It was a 3 Example! Type number of next Example: ")
    elif a == "4":
        print("----------------------------------------------------------------------------------------")
        print("Most Values are True")
        print("Almost any value is evaluated to True if it has some sort of content.\n")
        print("Any string is True, except empty strings.\n")
        print("Any number is True, except 0.\n")
        print("Any list, tuple, set, and dictionary are True, except empty ones.\n")

        print("----------------------------------------------------------------------------------------")
        print("Example")
        print("The following will return True:\n")

        print("----------------------------------------------------------------------------------------")
        print('bool("abc")')
        print(bool("abc"))

        print("----------------------------------------------------------------------------------------")
        print('bool(123)')
        print(bool(123))

        print("----------------------------------------------------------------------------------------")
        print('bool(["apple", "cherry", "banana"])')
        print(bool(["apple", "cherry", "banana"]))

        print("----------------------------------------------------------------------------------------")
        print("It was a 4 Example! Type number of next Example: ")
    elif a == "5":
        print("----------------------------------------------------------------------------------------")
        print("Some Values are False")
        print("In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, \"\", the number 0, and the value None. And of course the value False evaluates to False.\n")

        print("----------------------------------------------------------------------------------------")
        print("Example")
        print("The following will return False:\n")

        print("----------------------------------------------------------------------------------------")
        print('bool(False)')
        print(bool(False))

        print("----------------------------------------------------------------------------------------")
        print('bool(None)')
        print(bool(None))

        print("----------------------------------------------------------------------------------------")
        print('bool(0)')
        print(bool(0))

        print("----------------------------------------------------------------------------------------")
        print('bool("")')
        print(bool(""))

        print("----------------------------------------------------------------------------------------")
        print('bool(())')
        print(bool(()))

        print("----------------------------------------------------------------------------------------")
        print('bool([])')
        print(bool([]))

        print("----------------------------------------------------------------------------------------")
        print('bool({})')
        print(bool({}))
        """
        print("----------------------------------------------------------------------------------------")
        print("One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:\n")

        print("----------------------------------------------------------------------------------------")
        print("class myclass():")
        print("  def __len__(self):")
        print("    return 0\n")

        print("myobj = myclass()")
        print('print(bool(myobj))')
        myobj = myclass()
        print(bool(myobj))
        """
        print("----------------------------------------------------------------------------------------")
        print("It was a 5 Example! Type number of next Example: ")
    elif a == "6":
        print("----------------------------------------------------------------------------------------")
        print("Functions can Return a Boolean")
        print("You can create functions that returns a Boolean Value:\n")

        print("----------------------------------------------------------------------------------------")
        print("Example")
        print("Print the answer of a function:\n")

        print("----------------------------------------------------------------------------------------")
        print("def myFunction() :")
        print("  return True\n")

        print("print(myFunction())")
        def myFunction():
            return True
        print(myFunction())

        print("----------------------------------------------------------------------------------------")
        print("You can execute code based on the Boolean answer of a function:\n")

        print("----------------------------------------------------------------------------------------")
        print("Example")
        print("Print \"YES!\" if the function returns True, otherwise print \"NO!\":\n")

        print("----------------------------------------------------------------------------------------")
        print("def myFunction() :")
        print("  return True\n")

        print("if myFunction():")
        print("  print(\"YES!\")")
        print("else:")
        print("  print(\"NO!\")\n")

        if myFunction():
            print("YES!")
        else:
            print("NO!")

        print("----------------------------------------------------------------------------------------")
        print("Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:\n")

        print("----------------------------------------------------------------------------------------")
        print("Example")
        print("Check if an object is an integer or not:\n")

        print("----------------------------------------------------------------------------------------")
        print("x = 200")
        print("print(isinstance(x, int))\n")

        x = 200
        print(isinstance(x, int))

        print("----------------------------------------------------------------------------------------")
        print("It was a 6 Example! Type number of next Example: ")
    elif a == 'q':
        print("See you next time!")
        break
    else:
        print(" ")
        print("Eneter number between 1-6!")
