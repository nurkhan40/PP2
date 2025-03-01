import re 

with open(r"C:\Users\Nurhan\Desktop\PP2\lab_05\row-github.txt", "r") as f:
    data = f.read()

matches=re.sub(r"[A-Z]",'_',data)
print(matches)