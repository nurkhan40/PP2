import math

def sphere_volume(radius):
    return round(((4/3) * math.pi * (radius ** 3)), 2)

radius = int(input("Enter the radius of sphere: "))
print(sphere_volume(radius))