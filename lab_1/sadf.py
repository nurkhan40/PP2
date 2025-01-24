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
a = input("Number of Example: ")
if a == "1":
    print("How does code is looking: ")
    print("\\nif 5 > 2:")
    print('\\nprint("Five is greater than two!")')
    if 5 > 2:
        print("Five is greater than two!")
elif a == "2":
    if 5 > 2:
        print("Five is greater than two!")
