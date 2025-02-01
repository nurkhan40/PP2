"""
Python JSON
"""
"""
#-----------------------------------------------------
import json
#-----------------------------------------------------
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
#-----------------------------------------------------
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
#-----------------------------------------------------
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#-----------------------------------------------------
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
#-----------------------------------------------------
json.dumps(x, indent=4)
#-----------------------------------------------------
json.dumps(x, indent=4, separators=(". ", " = "))
#-----------------------------------------------------
json.dumps(x, indent=4, sort_keys=True)
#-----------------------------------------------------
"""

print("----------------------------------------------------------------------------------------")
print('Python JSON')

print("----------------------------------------------------------------------------------------")
print('Example 1: Importing JSON Module')

import json

print('import json')

print("----------------------------------------------------------------------------------------")
print('Example 2: Parsing JSON')

import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print('import json')
print('x = "{ \"name\":\"John\", \"age\":30, \"city\":\"New York\"}"')
print('y = json.loads(x)')
print('print(y["age"])')
print(y["age"])

print("----------------------------------------------------------------------------------------")
print('Example 3: Converting Python Object to JSON')

import json

x = {"name": "John", "age": 30, "city": "New York"}
y = json.dumps(x)

print('import json')
print('x = {"name": "John", "age": 30, "city": "New York"}')
print('y = json.dumps(x)')
print('print(y)')
print(y)

print("----------------------------------------------------------------------------------------")
print('Example 4: Converting Different Data Types to JSON')

import json

print('import json')
print('print(json.dumps({"name": "John", "age": 30}))')
print('print(json.dumps(["apple", "bananas"]))')
print('print(json.dumps(("apple", "bananas")))')
print('print(json.dumps("hello"))')
print('print(json.dumps(42))')
print('print(json.dumps(31.76))')
print('print(json.dumps(True))')
print('print(json.dumps(False))')
print('print(json.dumps(None))')
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("----------------------------------------------------------------------------------------")
print('Example 5: Formatting JSON Output')

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print('import json')
print('x = { ... complex JSON structure ... }')
print('print(json.dumps(x, indent=4))')
print(json.dumps(x, indent=4))

print("----------------------------------------------------------------------------------------")
print('Example 6: Customizing JSON Separators')

print('json.dumps(x, indent=4, separators=(". ", " = "))')
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print("----------------------------------------------------------------------------------------")
print('Example 7: Sorting JSON Keys')

print('json.dumps(x, indent=4, sort_keys=True)')
print(json.dumps(x, indent=4, sort_keys=True))

print("----------------------------------------------------------------------------------------")
