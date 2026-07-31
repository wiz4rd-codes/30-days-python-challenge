import time
from functools import lru_cache
movies = {
    "Interstellar": 8.7,
    "Inception": 8.8,
    "Avatar": 7.8,
    "Joker": 8.4
}
@lru_cache(maxsize=None)
def get_movie_rating(movie_name):
    print("Fetching rating...")
    time.sleep(5)
    return movies[movie_name]
name = input("Enter Movie Name : ")
print(get_movie_rating(name.capitalize()))
print(get_movie_rating(name.capitalize()))
