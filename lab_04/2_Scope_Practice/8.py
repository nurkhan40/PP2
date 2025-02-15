x = 1 
def outer():
    
    x = 2
    def inner():
        x = 3
        print(x)
        return
    inner()
    print(x)
    return
outer()
print(x)
