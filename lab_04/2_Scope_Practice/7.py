x = 1 
def outer():
    x = 2
    def inner():
        nonlocal x
        x = 3
        print(x)
        return
    inner()
    print(x)
    return
outer()
print(x)
