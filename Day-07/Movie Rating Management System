class MovieTicket : 
    def __init__(self,name ,rate):
        self.movie_name = name 
        self.rate = rate
    
    @property
    def rating(self):
        return self.rate
    
    @rating.setter
    def rating(self, rate):
        self.rate = rate if rate in range(0,11) else "Invalid rating"

    def display(self):
        print(f"Name of the movie : {self.movie_name}")
        print(f"Rating : {self.rating}")
n = int(input("How many movies you want to enter : "))
movies = []
for i in range(0,n):
    name = input(f"Enter name of the movie {i+1} : ")
    rating = int(input("Rate this movie from 0 to 10 : "))
    movie = MovieTicket(name,rating)
    movies.append(movie)
for i,movie in enumerate(movies, start = 1):
    print(f"Movie number : {i}")
    movie.display()
c = input("Do you want to change rating of any movie ?\nEnter \"Yes\' or \"No\" : ")
if(c.capitalize() == "Yes"):
    cn = int(input("Enter Movie number whose rating you want to change : "))
    nr = int(input("Enter new rating : "))
    movies[cn-1].rating = nr
    print(f"Rating changed successfully\nNew data of Movie number : {cn}")
    movies[cn-1].display()
