def grams_to_ounces(grams):
    return round(grams * 28.3495231, 2)

grams = float(input("Enter the amount of grams: "))
print(f"{grams} gram is equal to {grams_to_ounces(grams)} ounces")