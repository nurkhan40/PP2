"""

Python Data Types

Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
    Text Type:	        str
    Numeric Types:	    int, float, complex
    Sequence Types:	    list, tuple, range
    Mapping Type:	    dict
    Set Types:	        set, frozenset
    Boolean Type:	    bool
    Binary Types:   	bytes, bytearray, memoryview
    None Type:	        NoneType
"""

print("Enter the number of example: ")
print("Enter 'q' to leave")
print("1. Getting Data Type\n2. Setting the Data Type")

while True:
    a = input()

    if a == "1":
        print("----------------------------------------")
        print("Getting the Data Type")
        print("The code and You can get the data type of any object by using the type() function.")
        print('Print the data type of the variable x:')
        print('x = 5\nprint(type(x))')
        print(" ")
        print("The answer: ")
        x = 5
        print(type(x))
        print("----------------------------------------")
    elif a == "2":
            print("----------------------------------------")
            print("Setting the Data Type\n")
            print("The codes and In Python, the data type is set when you assign a value to a variable.")
            print("Note: There are more than 15 built-in data types in Python!\n")
            print("1. str (Text Type)")
            print("2. int (Integer Type)")
            print("3. float (Floating Point Type)")
            print("4. complex (Complex Number Type)")
            print("5. list (Sequence Type)")
            print("6. tuple (Sequence Type)")
            print("7. range (Sequence Type)")
            print("8. dict (Mapping Type)")
            print("9. set (Set Type)")
            print("10. frozenset (Set Type)")
            print("11. bool (Boolean Type)")
            print("12. bytes (Binary Type)")
            print("13. bytearray (Binary Type)")
            print("14. memoryview (Binary Type)")
            print("15. NoneType (None Type)")
            print("'q' Leave")
            print("----------------------------------------")
            while True:
                b = input()
                if b == "1":
                    print("----------------------------------------")
                    print("The code data type 'str'\n")
                    print('x = "Hello World"\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n')
                    print("The output\n")
                    x = "Hello World"
                    print(x)
                    print(type(x))
                    print("----------------------------------------")
                elif b == "2":
                    print("----------------------------------------")
                    print("The code data type 'int'\n")
                    print('x = 20\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n')
                    print("The output\n")
                    x = 20
                    print(x)
                    print(type(x))
                    print("----------------------------------------")
                elif b == "3":
                    print("----------------------------------------")
                    print("The code data type 'float'\n")
                    print('x = 20.5\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n')
                    print("The output\n")
                    x = 20.5
                    print(x)
                    print(type(x))
                    print("----------------------------------------")
                elif b == "4":
                    print("----------------------------------------")
                    print("The code data type 'complex'\n")
                    print('x = 1j\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n')
                    print("The output\n")
                    x = 1j
                    print(x)
                    print(type(x))
                    print("----------------------------------------")
                elif b == "5":
                    print(" ")
                    print("The code data type 'list'\n")
                    print('x = ["apple", "banana", "cherry"]\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n')
                    print("The output\n")
                    x = ["apple", "banana", "cherry"]
                    print(x)
                    print(type(x))
                    print("----------------------------------------")
                elif b == "6":
                    print("----------------------------------------")
                    print("The code data type 'tuple'\n")
                    print('x = ("apple", "banana", "cherry")\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n')
                    print("The output\n")
                    x = ("apple", "banana", "cherry")
                    print(x)
                    print(type(x))
                    print("----------------------------------------")
                elif b == "7":
                    print(" ")
                    print("The code data type 'range'\n")
                    print('x = range(6)\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n')
                    print("The output\n")
                    x = range(6)
                    print(x)
                    print(type(x))
                    print("----------------------------------------")
                elif b == "8":
                    print("----------------------------------------"); print("The code data type 'dict'\n"); print('x = {"name" : "John", "age" : 36}\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = {"name" : "John", "age" : 36}; print(x); print(type(x)); print("----------------------------------------")
                elif b == "9":
                    print("----------------------------------------"); print("The code data type 'set'\n"); print('x = {"apple", "banana", "cherry"}\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = {"apple", "banana", "cherry"}; print(x); print(type(x)); print("----------------------------------------")
                elif b == "10":
                    print("----------------------------------------"); print("The code data type 'frozenset'\n"); print('x = frozenset({"apple", "banana", "cherry"})\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = frozenset({"apple", "banana", "cherry"}); print(x); print(type(x)); print("----------------------------------------")
                elif b == "11":
                    print("----------------------------------------"); print("The code data type 'bool'\n"); print('x = True\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = True; print(x); print(type(x)); print("----------------------------------------")
                elif b == "12":
                    print("----------------------------------------"); print("The code data type 'bytes'\n"); print('x = b"Hello"\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = b"Hello"; print(x); print(type(x)); print("----------------------------------------")
                elif b == "13":
                    print("----------------------------------------"); print("The code data type 'NoneType'\n"); print('x = None\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = None; print(x); print(type(x)); print("----------------------------------------")
                elif b == "14":
                    print("----------------------------------------"); print("The code data type 'bytearray'\n"); print('x = bytearray(5)\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = bytearray(5); print(x); print(type(x)); print("----------------------------------------")
                elif b == "15":
                    print("----------------------------------------"); print("The code data type 'memoryview'\n"); print('x = memoryview(bytes(5))\n\n# display x:\nprint(x)\n\n# display the data type of x:\nprint(type(x))\n'); print("The output\n"); x = memoryview(bytes(5)); print(x); print(type(x)); print("----------------------------------------")
                elif b == "q":
                    print("Enter the number of example: ")
                    print("Enter 'q' to leave")
                    print("1. Getting Data Type\n2. Setting the Data Type")

                    break
                else:
                    print("Enter number between 1-15 or 'q' to leave!")
    elif a == 'q':
        print("See you next time!")
        break
    else:
        print("----------------------------------------")
        print("Enter number between 1-2 or 'q' to leave!")
        print('----------------------------------------')