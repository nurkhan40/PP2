import re

with open(r"C:\Users\Nurhan\Desktop\PP2\lab_05\row-9-exercise.txt", "r") as f:
    data = f.read()

print(re.findall(r"[A-Z][a-z]*", data))