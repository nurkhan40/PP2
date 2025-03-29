a = input()
new_word = ""
for char in a:
    if char.isalpha() or char == " ":
        new_word += char

print(new_word)