# pip install IMDbPY
import imdb
a = imdb.IMDb()
movie_name = input("Enter the name of movie: ")
movies = a.search_movie((movie_name))
index = movies[0].getID()
movie = a.get_movie(index)
movie_title = movie['title']
movie_year = movie['year']
movie_cast = movie['cast']

s = len(movie_cast)

print("title of the movie is: ",movie_title)
print("Year of release of the movie is: ",movie_year)
print("The cast of the movie is: ")

for i in range(0,s):
    movie_cast_name=movie_cast[i]['name']
    print(" "+movie_cast_name)
