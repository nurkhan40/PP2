"""
Python While Loops
"""
#-----------------------------------------------------
i = 1
while i < 6:
  print(i)
  i += 1
#-----------------------------------------------------
i1 = 1
while i1 < 6:
  print(i1)
  if i1 == 3:
    break
  i1 += 1
#-----------------------------------------------------
i2 = 0
while i2 < 6:
  i2 += 1
  if i2 == 3:
    continue
  print(i2)
#-----------------------------------------------------
i3 = 1
while i3 < 6:
  print(i3)
  i3 += 1
else:
  print("i is no longer less than 6")
#-----------------------------------------------------