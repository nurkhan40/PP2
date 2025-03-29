a = input()
new_word = ""

for char in a:
    if char.islower() or char == " ":
        new_word += char

print(new_word)