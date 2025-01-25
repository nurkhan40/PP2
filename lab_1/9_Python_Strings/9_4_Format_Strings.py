"""
Python - Format - Strings
"""

print("----------------------------------------------------------------------------------------\n")
print("The code data type 'String Format'\n")
print("As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:\n")
print("Example:\n")
print("age = 36\n")
print('txt = "My name is John, I am " + age\n')
print("print(txt)\n")
print("The output\n")
print("This will raise an error because you cannot concatenate a string and an integer directly.")
print("But we can combine strings and numbers by using f-strings or the format() method!")

print("----------------------------------------------------------------------------------------\n")
print("The code data type 'F-Strings'\n")
print("F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.\n")
print("To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.\n")
print("Example:\n")
print("Create an f-string:\n")
print("age = 36\n")
print('txt = f"My name is John, I am {age}"\n')
print("print(txt)\n")
print("The output\n")

# Example:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

print("----------------------------------------------------------------------------------------\n")
print("The code data type 'Placeholders and Modifiers'\n")
print("A placeholder can contain variables, operations, functions, and modifiers to format the value.\n")
print("Example:\n")
print("Add a placeholder for the price variable:\n")
print("price = 59\n")
print('txt = f"The price is {price} dollars"\n')
print("print(txt)\n")
print("The output:\n")

# Example:
price = 59
txt = f"The price is {price} dollars"
print(txt)

print("----------------------------------------------------------------------------------------\n")
print("Display the price with 2 decimals:\n")
print("Example:\n")
print("price = 59\n")
print('txt = f"The price is {price:.2f} dollars"\n')
print("print(txt)\n")
print("The output:\n")

# Example:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

print("\n----------------------------------------------------------------------------------------\n")
print("Perform a math operation in the placeholder, and return the result:\n")
print("Example:\n")
print('txt = f"The price is {20 * 59} dollars"\n')
print("print(txt)\n")
print("The output:\n")

# Example:
txt = f"The price is {20 * 59} dollars"
print(txt)

print("\n----------------------------------------------------------------------------------------")
