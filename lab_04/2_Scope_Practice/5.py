x = 1
def foo():
    global x
    x = 11
    y = 12
    print(x)
    print(y)
foo()
print(x)