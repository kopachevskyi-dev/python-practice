"""
The user should be able to:
- Add a new movie to the collection
- See all movies in the collection
- Find a movie by its title

How to build it:
- Decide where to store the movies in the code
- Decide what information to save for each movie
- Show a menu and let the user choose an option
- Write each feature as its own function
- Stop the program when the user types 'q'
"""

# Movie collection
movie_collection = []

# Adds a new movie to the collection
def add_new_movie(movie_title, movie_director, movie_year):
    movie = {
        'title': movie_title,
        'director': movie_director,
        'year': movie_year
    }

    movie_collection.append(movie)

# Lists current collection
def list_movie_collection(movie_collection):
    print('Your current movie collection: ')

    for movie in movie_collection:
        print(movie)
