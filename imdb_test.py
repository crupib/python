# IMDB
# pip install imdbpy
import imdb
ia = imdb.IMDb()
# Search for a movie.
search_result = ia.search_movie('The Matrix')
# Get the ID of the movie.
movie_id = search_result[0].movieID
# Get the movie from ID
movie = ia.get_movie(movie_id)
# Get Rating of movie
rating = movie['rating']
# Get Plot of movie
plot = movie['plot']
# Get Genre of movie
genre = movie['genres']
# Get Box office of movie
box_office = movie['box office']
# Get Cast of movie
cast = movie['cast']
# Get Director of movie
director = movie['director']
# Get Writer of movie
writer = movie['writer']
# Search for a person.
search_result = ia.search_person('Keanu Reeves')
print(search_result)
