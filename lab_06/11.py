word = input()
space = word.count(" ")
letters = sum(char.isalpha() for char in word)
numbers = sum(char.isdigit() for char in word)

print(numbers)
print(space)
print(letters)