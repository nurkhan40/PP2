"""
Python Strings
"""

#Strings
print("----------------------------------------------------------------------------------------")
print("Strings")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("print(\"Hello\")")
print("print('Hello')")
print("")
print("The output:")
print("Hello")
print("Hello")
print("----------------------------------------------------------------------------------------")

#Quotes Inside Quotes
print("----------------------------------------------------------------------------------------")
print("Quotes Inside Quotes")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("print(\"It's alright\")")
print("print(\"He is called 'Johnny'\")")
print("print('He is called \"Johnny\"')")
print("")
print("The output:")
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print("----------------------------------------------------------------------------------------")

#Assign String to a Variable
print("----------------------------------------------------------------------------------------")
print("Assign String to a Variable")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("a = \"Hello\"")
print("print(a)")
print("")
print("The output:")
a = "Hello"
print(a)
print("----------------------------------------------------------------------------------------")

#Multiline Strings
print("----------------------------------------------------------------------------------------")
print("Multiline Strings")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("a = \"\"\"Lorem ipsum dolor sit amet,")
print("consectetur adipiscing elit,")
print("sed do eiusmod tempor incididunt")
print("ut labore et dolore magna aliqua.\"\"\"")
print("print(a)")
print("")
print("The output:")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("----------------------------------------------------------------------------------------")
print("Or three single quotes:")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("a = '''Lorem ipsum dolor sit amet,")
print("consectetur adipiscing elit,")
print("sed do eiusmod tempor incididunt")
print("ut labore et dolore magna aliqua.'''")
print("print(a)")
print("")
print("The output:")
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("Note: in the result, the line breaks are inserted at the same position as in the code.")
print("----------------------------------------------------------------------------------------")

#Strings are Arrays
print("----------------------------------------------------------------------------------------")
print("Strings are Arrays")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("a = \"Hello, World!\"")
print("print(a[1])")
print("")
print("The output:")
a = "Hello, World!"
print(a[1])
print("----------------------------------------------------------------------------------------")

#Looping Through a String
print("----------------------------------------------------------------------------------------")
print("Looping Through a String")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("for x in \"banana\":")
print("  print(x)")
print("")
print("The output:")
for x in "banana":
    print(x)
print("----------------------------------------------------------------------------------------")

#String Length
print("----------------------------------------------------------------------------------------")
print("String Length")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("a = \"Hello, World!\"")
print("print(len(a))")
print("")
print("The output:")
a = "Hello, World!"
print(len(a))
print("----------------------------------------------------------------------------------------")

#Check String
print("----------------------------------------------------------------------------------------")
print("Check String")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("txt = \"The best things in life are free!\"")
print("print(\"free\" in txt)")
print("")
print("The output:")
txt = "The best things in life are free!"
print("free" in txt)
print("----------------------------------------------------------------------------------------")

print("----------------------------------------------------------------------------------------")
print("Use it in an if statement:")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("txt = \"The best things in life are free!\"")
print("if \"free\" in txt:")
print("    print(\"Yes, 'free' is present.\")")
print("")
print("The output:")
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print("----------------------------------------------------------------------------------------")

#Check if NOT
print("----------------------------------------------------------------------------------------")
print("Check if NOT")
print("----------------------------------------------------------------------------------------")
print("Example")
print("")
print("The code:")
print("txt = \"The best things in life are free!\"")
print("print(\"expensive\" not in txt)")
print("")
print("The output:")
txt = "The best things in life are free!"
print("expensive" not in txt)

print("----------------------------------------------------------------------------------------")
print("Use it in an if statement:")
print("----------------------------------------------------------------------------------------")
print("The code:")
print("txt = \"The best things in life are free!\"")
print("if \"expensive\" not in txt:")
print("    print(\"No, 'expensive' is NOT present.\")")
print("")
print("The output:")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
print("----------------------------------------------------------------------------------------")