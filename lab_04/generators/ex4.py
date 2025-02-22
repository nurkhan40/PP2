def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2  

for square in squares(2, 6):
    print(square)