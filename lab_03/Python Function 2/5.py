from moviess import movies

def imdb(movies):
    category = input("category: ")
    c = list()
    for movie in movies:
        if movie["category"] == category:
            c.append(movie["imdb"])
    if len(c) == 0:
        return 0
    
    b = sum(c) / len(c)
    return round(b, 2)

print(imdb(movies))