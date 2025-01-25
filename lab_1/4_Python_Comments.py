"""
Python Comments

Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

"""

"""
Creating a Comment

Comments starts with a #, and Python will ignore them.
There are 3 exmaples
"""
"""
Multiline Comments

Python does not really have a syntax for multiline comments.
"""
print("Enter the number of an Example!")
print("Enter 'q' to leave!")
while True:
    a = input()
    if a == "1":
        print(" ")
        print("#This is a comment")
        #This one actually
        print('print("Hello, World!")')
        print(" ")
    elif a == "2":
        print(" ")
        print("Comments can be placed at the end of a line, and Python will ignore the rest of the line")
        print(" ")
        print('print("Hello, World!") #This is a comment')
        print(" ")
    elif a == "3":
        print(" ")
        print("A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code")
        print(" ")
        print('#print("Hello, World!")')
        print('print("Cheers, Mate!"')
        print(" ")
    elif a == "4":
        print(" ")
        print("To add a multiline comment you could insert a # for each line:")
        print(" ")
        print("#This is a comment")
        print("#written in")
        print("#more than just one line")
        print('print("Hello, World!")')
        print(" ")
    elif a == "5":
        print(" ")
        print("Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it")
        print(" ")
        print('"""')
        print("This is a comment")
        print("written in")
        print("more than just one line")
        print('"""')
        print('print("Hello, World!")')
        print(" ")
        print("As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.")
        print(" ")
    elif a == "q":
        break
    else:
        print(" ")
        print("enter a number between 1-5 or 'q'")
        print(" ")