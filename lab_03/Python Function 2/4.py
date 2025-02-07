from moviess import movies

def avrg(movies):
    a = list()
    for movie in movies:
        if movie["imdb"] > 0:
            a.append(movie["imdb"])
    
    if len(a) == 0:
        return 0  
    
    b = sum(a) / len(a)
    return round(b, 2)

print(avrg(movies))
