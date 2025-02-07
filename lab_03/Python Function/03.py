def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return 0, 0
    
a, b = solve(35, 94)
print(f"Chickens: {a}, Rabbits :{b}")