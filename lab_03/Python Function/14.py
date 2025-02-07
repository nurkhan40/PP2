import random
from math import pi
import re

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4/3) * pi * (radius ** 3)

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(s):
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_s == cleaned_s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    attempts = 0
    while True:
        print("\nTake a guess.")
        try:
            guess = int(input())
            attempts += 1
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    print("spy_game([1, 2, 4, 0, 0, 7, 5]) ->", spy_game([1, 2, 4, 0, 0, 7, 5]))
    
    print("sphere_volume(3) ->", sphere_volume(3))
    
    print("unique_elements([1, 2, 3, 3, 2, 1, 4, 5]) ->", unique_elements([1, 2, 3, 3, 2, 1, 4, 5]))
    
    print("is_palindrome('A man, a plan, a canal, Panama') ->", is_palindrome("A man, a plan, a canal, Panama"))
    
    print("Histogram output:")
    histogram([4, 9, 7])
    
    # Run the guess_the_number game
    # Uncomment the line below to play
    # guess_the_number()