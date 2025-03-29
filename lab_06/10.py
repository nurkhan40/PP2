word = input()
a = "aeuioAEUIO"
new_word = []

for letter in word:
    if letter not in a:
        new_word += letter

print(''.join(new_word))