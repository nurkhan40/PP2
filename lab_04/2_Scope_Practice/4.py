#Scope

def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "Hello"
    myfunc2()
    return x

print(myfunc1())