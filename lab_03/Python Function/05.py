from itertools import permutations

def string_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    for p in perms:
        print(p)

a = input("Enter a string: ")
print("Permutations of the string are: ")
string_permutations(a)