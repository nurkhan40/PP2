from moviess import movies

def list_of_losers(movies):
    a = list()

    for movie in movies:
        if movie["imdb"] < 5.5:
            a.append(movie["name"])
    return a

print(list_of_losers(movies))