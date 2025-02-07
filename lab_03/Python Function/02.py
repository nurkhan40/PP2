def temperature(temp):
    c = (5/9) * (temp - 32)
    return round(c, 2)

temp = float(input("Enter temperature in Fahrenheit: "))
c = temperature(temp)
print(f"The equivalent Celcuis temperature is: {c}C")