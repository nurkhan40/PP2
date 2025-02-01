"""
Access Items
"""
#-----------------------------------------------------------------
thislist1 = ["apple", "banana", "cherry"]
print(thislist1[1])
#-----------------------------------------------------------------
thislist2 = ["apple", "banana", "cherry"]
print(thislist2[-1])
#-----------------------------------------------------------------
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5])
#-----------------------------------------------------------------
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[:4])
#-----------------------------------------------------------------
thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[2:])
#-----------------------------------------------------------------
thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist6[-4:-1])
#-----------------------------------------------------------------
thislist7 = ["apple", "banana", "cherry"]
if "apple" in thislist7:
  print("Yes, 'apple' is in the fruits list")
#-----------------------------------------------------------------