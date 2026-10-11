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
        print("Your current movie collection:")

        for movie in movie_collection:
            print(f"- {movie['title']} ({movie['year']}), director: {movie['director']}")
    else:
        print("Your current collection is empty.")

# Search a movie from the collection based on it's title
def search_movie(title, movie_collection):
    for movie in movie_collection:
        if title.strip().lower() == movie["title"].lower():
            print("The movie you are looking for is:")
            print(f"- {movie['title']} ({movie['year']}), director: {movie['director']}")
            break
    else:
        print("Can't find a movie with that title in your collection.")

print(
"""
WELCOME TO THE MOVIE COLLECTION APP

- Enter 'add' to add a new movie
- Enter 'list' to show your collection
- Enter 'search' to find a movie by title
- Enter 'q' to quit
""")

while True:
    user_input = input("\nYour choice (add / list / search / q): ").strip().lower()

    if user_input == "add":
        movie_title = input("Movie title: ").strip()
        movie_director = input("Director: ").strip()
        movie_year = input("Release year: ").strip()

        if not movie_title or not movie_director or not movie_year.isdigit():
            print("Incorrect movie data. Title and director are required, and the year must be a whole number.")
        else:
            add_new_movie(movie_title, movie_director, int(movie_year))
            print(f"Added: {movie_title} ({movie_year}), director: {movie_director}.")
    elif user_input == "list":
        list_movie_collection(movie_collection)
    elif user_input == "search":
        title = input("Movie title: ").strip()

        if not title.strip():
            print("Incorrect movie title. Enter a title to search for.")
        else:
            search_movie(title, movie_collection)
    elif user_input == "q":
        print("See ya later, bye!")
        break
    else:
        print("Incorrect input. Enter 'add', 'list', 'search', or 'q'.")
