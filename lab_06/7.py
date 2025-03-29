word = input()
vov = "aioueAIOUE"
new_word = []
for letter in word:
    if letter not in vov:
        new_word += letter

print(new_word)