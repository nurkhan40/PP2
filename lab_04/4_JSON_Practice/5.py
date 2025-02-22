import json

x = {
    "name" : "Nurkhan",
    "age" : 18,
    "married" : False,
    "pets" : "cat",
    "cars" : [
        {
            "model" : "BMW 960", "mpg" : 27.5
        },
        {
            "model" : "Mercedec S Series", "mpg" : 24.1
        }
    ]
}

print(json.dumps(x, indent=4))