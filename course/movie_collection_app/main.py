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
- Stop the program when the user types "q"
"""

# Movie collection
movie_collection = []

# Adds a new movie to the collection
def add_new_movie(movie_title, movie_director, movie_year):
    movie = {
        "title": movie_title,
        "director": movie_director,
        "year": movie_year
    }

    movie_collection.append(movie)

# Lists current collection
def list_movie_collection(movie_collection):
    if len(movie_collection) != 0:
        print("Your current movie collection: ")

        for movie in movie_collection:
            print(movie)
    else:
        print("Your current collection is empty :(")

# Search a movie from the collection based on it's title
def search_movie(title, movie_collection):
    for index, movie in enumerate(movie_collection):
        if title.lower() == movie["title"].lower():
            print("The movie you are looking for is: ")
            print(movie)
        else:
            print("Can't find a movie with such title in your collection :(")

print(
"""
WELCOME TO THE MOVIE COLLECTION APP

1. Enter 'add' if you want to add a new movie to the collection
2. Enter 'list' if you want to list you current movie collection
3. Enter 'search' if you want to search for a specific movie from your collection
4. Enter 'q' if you want to quit the app

""")

while (True):
    user_input = input("Your choice: ")

    if user_input == "add":
        # Input
        movie_title = input("Please provide a movie title: ")
        movie_director = input("Please provide a name of the movie director: ")
        movie_year = input("Please provide a year when the movie was released: ")
        # Logic
        add_new_movie(movie_title, movie_director, movie_title)
    elif user_input == "list":
        # Logic
        list_movie_collection(movie_collection)
    elif user_input == "search":
        # Input
        title = input("Please provide a movie title: ")
        # Logic
        search_movie(title, movie_collection)
    elif user_input == "q":
        print("See ya later, bye!")
        break
    else:
        print("Incorrect input, please try again")
