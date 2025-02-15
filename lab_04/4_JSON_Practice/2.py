import json
x = '{"name" : "Nurkhan", "age" : 18 , "country" : "Kazakhstan"}'

y = json.loads(x)
print(y["age"])