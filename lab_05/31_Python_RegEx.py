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

"""
Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
"""

"""
Character	Description	                                    Example
[]	        A set of characters	                            "[a-m]"	
\	        Signals a special sequence	                    "\d"	
.	        Any character (except newline character)	    "he..o"	
^	        Starts with	                                    "^hello"	
$	        Ends with	                                    "planet$"	
*	        Zero or more occurrences	                    "he.*o"	
+	        One or more occurrences	                        "he.+o"	
?	        Zero or one occurrences	                        "he.?o"	
{}	        Exactly the specified number of occurrences	    "he.{2}o"	
|	        Either or	                                    "falls|stays"	
()	        Capture and group	 
"""

"""
Character	Description	                                                                                            Example

\A	        Returns a match if the specified characters are at the beginning of the string	                        "\AThe"	
\b	        Returns a match where the specified characters are at the beginning or at the end of a word             r"\bain"
            (the "r" in the beginning is making sure that the string is being treated as a "raw string")	        r"ain\b"	

\B	        Returns a match where the specified characters are present, but NOT at the beginning (or at the end)    r"\Bain"
            of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"ain\B"	

\d	        Returns a match where the string contains digits (numbers from 0-9)	                                    "\d"	
\D	        Returns a match where the string DOES NOT contain digits	                                            "\D"	
\s	        Returns a match where the string contains a white space character	                                    "\s"	
\S	        Returns a match where the string DOES NOT contain a white space character	                            "\S"	
\w	        Returns a match where the string contains any word characters (characters from a to Z, 
            digits from 0-9, and the underscore _ character)	                                                    "\w"	
\W	        Returns a match where the string DOES NOT contain any word characters	                                "\W"	
\Z	        Returns a match if the specified characters are at the end of the string	                            "Spain\Z"
"""

"""
Set	            Description

[arn]	        Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	        Returns a match for any lower case character, alphabetically between a and n	
[^arn]	        Returns a match for any character EXCEPT a, r, and n	
[0123]	        Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	        Returns a match for any digit between 0 and 9	
[0-5][0-9]	    Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	            In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
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
