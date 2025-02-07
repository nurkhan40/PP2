def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numb):
    return [num for num in numb if is_prime(num)]

numbers = list(map(int, input("Enter numbers seperated by spaces: ").split()))
primes = filter_prime(numbers)
print(f"Prime numbers: {primes}")
