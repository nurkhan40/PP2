"""
Remove List Items
"""
#-------------------------------------------
thislist1 = ["apple", "banana", "cherry"]
thislist1.remove("banana")
print(thislist1)
#-------------------------------------------
thislist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist2.remove("banana")
print(thislist2)
#-------------------------------------------
thislist3 = ["apple", "banana", "cherry"]
thislist3.pop(1)
print(thislist3)
#-------------------------------------------
thislist4 = ["apple", "banana", "cherry"]
thislist4.pop()
print(thislist4)
#-------------------------------------------
thislist5 = ["apple", "banana", "cherry"]
del thislist5[0]
print(thislist5)
#-------------------------------------------
thislist6 = ["apple", "banana", "cherry"]
del thislist6
#-------------------------------------------
thislist7 = ["apple", "banana", "cherry"]
thislist7.clear()
print(thislist7)
#-------------------------------------------