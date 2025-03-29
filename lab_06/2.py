def polindrom(b):
    if b == b[::-1]:
        print("YES")
        return True
    else:
        print("NO")
        return False

a = input()
polindrom(a)