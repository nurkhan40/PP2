"""
Python - Variable Names

Variable Names

A variable can have a short name (like x and y) 
or a more descriptive name (age, carname, total_volume). 
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

See more in Example 1!
"""



"""
Multi Words Variable Names

Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case.
Pascal Case.
Snake Case.

See more in Examples 2-4
"""

print("Enter the number of example: ")
print("Enter 'q' to leave")

while True:
    a = input()

    if a == "1":
        print('')
        print('Legal variable names:')
        print('myvar = "John"')
        print('my_var = "John"')
        print('_my_var = "John"')
        print('myVar = "John"')
        print('MYVAR = "John"')
        print('myvar2 = "John"')
        print('')
        print('Illegal variable names:')
        print('2myvar = "John"')
        print('my-var = "John"')
        print('my var = "John"')
        print('')
    elif a == "2":
        print('')
        print('Camel Case')
        print('Each word, except the first, starts with a capital letter:')
        print('myVariableName = "John"')
        print('')
    elif a == "3":
        print('')
        print('Pascal Case')
        print('Each word starts with a capital letter:')
        print('MyVariableName = "John"')
        print('')
    elif a == "4":
        print('')
        print('Snake Case')
        print('Each word is separated by an underscore character:')
        print('my_variable_name = "John"')
        print('')
    elif a == 'q':
        print("See you next time!")
        break
    else:
        print(" ")
        print("Eneter number between 1-4 or 'q' to leave!")
        print(" ")