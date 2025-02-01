"""
Python RegEx
"""
"""
#-----------------------------------------------------
import re
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
#-----------------------------------------------------
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an objec


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())



import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
"""

print("----------------------------------------------------------------------------------------")
print('Python RegEx')

print("----------------------------------------------------------------------------------------")
print('Example 1: Importing re Module')

import re

print('import re')

print("----------------------------------------------------------------------------------------")
print('Example 2: Searching for a Pattern')

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print('import re')
print('txt = "The rain in Spain"')
print('x = re.search("^The.*Spain$", txt)')

print("----------------------------------------------------------------------------------------")
print('Example 3: Finding All Matches')

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print('x = re.findall("ai", txt)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 4: No Match Found')

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print('x = re.findall("Portugal", txt)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 5: Finding First White-Space Character')

import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print('x = re.search("\\s", txt)')
print('print("The first white-space character is located in position:", x.start())')
print("The first white-space character is located in position:", x.start())

print("----------------------------------------------------------------------------------------")
print('Example 6: Searching for a Non-Existent Pattern')

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print('x = re.search("Portugal", txt)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 7: Splitting a String')

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print('x = re.split("\\s", txt)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 8: Splitting with Max Split Limit')

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print('x = re.split("\\s", txt, 1)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 9: Replacing Characters')

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print('x = re.sub("\\s", "9", txt)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 10: Replacing Characters with Count')

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print('x = re.sub("\\s", "9", txt, 2)')
print('print(x)')
print(x)

print("----------------------------------------------------------------------------------------")
print('Example 11: Searching for a Substring')

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print('x = re.search("ai", txt)')
print('print(x) # this will print an object')
print(x) # this will print an object

print("----------------------------------------------------------------------------------------")
print('Example 12: Finding Word Boundaries')

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print('x = re.search(r"\\bS\\w+", txt)')
print('print(x.span())')
print(x.span())

print("----------------------------------------------------------------------------------------")
print('Example 13: Getting the Original String')

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print('print(x.string)')
print(x.string)

print("----------------------------------------------------------------------------------------")
print('Example 14: Getting the Matched Word')

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print('print(x.group())')
print(x.group())

print("----------------------------------------------------------------------------------------")
