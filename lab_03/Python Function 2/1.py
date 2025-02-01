from moviess import movies

def imdb(movies):
    name = input("name: ")

    for movie in movies:
        if movie["name"]==name:
            if movie["imdb"]>5.5:
                return True
    return False

print(imdb(movies))