"""
Execute Python Syntax

As we learned in the previous page, 
Python syntax can be executed by writing 
directly in the Command Line:

print("Hello, World!")
Hello, World!

Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:

C:\\Users\\Your Name>python myfile.py
"""

"""
Python Indentation

Indentation refers to the spaces at the 
beginning of a code line.

Where in other programming languages the 
indentation in code is for readability only, 
the indentation in Python is very important.

Python uses indentation to indicate a block of code.

Example 1
type "1" to provide
"""
while True:
    
    a = input("Number of Example (1-6): ")
    print(" ")

    if a == "1":
        print(" ")
        print("How does code is looking: ")
        print(" ")
        print("if 5 > 2:")
        print('    print("Five is greater than two!")')
        print(" ")
        print("The answer: ")
        print(" ")
        if 5 > 2:
            print("Five is greater than two!")
        print(" ")
    elif a == "2":
        print(" ")
        print("How does code is looking: ")
        print(" ")
        print("if 5 > 2:")
        print('print("Five is greater than two!")')
        print(" ")
        print("The answer is wrong because VScode won't give a permission to execute the code")
        print(" ")
    elif a == "3":
        print(" ")
        print("How does codes are looking: ")
        print("1: ")
        print("if 5 > 2:")
        print(' print("Five is greater than two!")')
        print("2: ")
        print("if 5 > 2:")
        print('         print("Five is greater than two!")')
        print(" ")
        print("The answers: ")
        if 5 > 2:
            print("Five is greater than two!")
        if 5 > 2:
            print("Five is greater than two!")
        print(" ")
    elif a == "4":
        print(" ")
        print("How does code is looking: ")
        print(" ")
        print("if 5 > 2:")
        print(' print("Five is greater than two!")')
        print('      print("Five is greater than two!")')
        print(" ")
        print("The answer is wrong because VScode won't give a permission to execute the code")
        print(" ")
    elif a == "5":
        print("Python Variables")
        print("How does code is looking: ")
        print(" ")
        print("x = 5")
        print('"Hello, World!"')
        print(" ")
        print("Python has no command for declaring a variable.")
        print(" ")
    elif a == "6":
        print("Comments")
        print("How does code is looking: ")
        print(" ")
        print("#This is a comment")
        #This one actually!
        print('"Hello, World!"')
        print(" ")
        print("Python has commenting capability for the purpose of in-code documentation.")
        print("Comments start with a #, and Python will render the rest of the line as a comment.")
        print(" ")
    elif a == "q":
        break
    else:
        print("Choose between 1-6 mate!")
    print("If you want quit then enter 'q' value")