#   A basic movie recommendation code using average for a single user
#   This code is based on the netflix-style-recommender project shared on GitHub.
#   It was written by Nikhil22.
#   The code has been modified from its original version.

# define the movies, users, and different ratings
movies = ["Back to the Future", "Guardians of the Galaxy", "Avatar", "Trolls", "Black Panther"]
genres = ["Action", "Adventure", "Science Fiction", "Comedy"]


# data from the book
# each row is a movie, each column is a genre
movie_genre = [
    [0.6, 0.0, 0.3, 0.1], 
    [0.2, 0.3, 0.3, 0.2],
    [0.3, 0.3, 0.4, 0.0], 
    [0.7, 0.0, 0.0, 0.3], 
    [0.1, 0.6, 0.3, 0.0]
]



# TODO rank the movies here (5 movies), 0 to 10
movie_ratings = []

# TODO rank the genres here (4 genres), 1 to 10
user_preferences = []




# get the estimated rating for a specific movie
for movie in range(len(movies)):
    rating = 0
    for genre in range(len(genres)):
        rating += user_preferences[genre] * movie_genre[movie][genre]
    print(movies[movie], "recommended rating: ", rating) 
    print("actual ranking was", movie_ratings[movie])
    print()

