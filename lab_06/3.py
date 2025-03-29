numbers = input()
num_list = list(map(int, numbers.split()))
odd = []
for num in num_list:
    if num % 2 != 0:
        odd.append(num)

print(odd)