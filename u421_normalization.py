#   a421_multi_movie_recommender.py
#   A basic movie recommendation code with normalization.
#   This code is based on the netflix-style-recommender project shared on GitHub.
#   All statistical functions were written by Nikhil22.
#   The code has been modified from its original version.
import numpy as np 

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


# TODO change these values to the names of the students in your group
users = ["jo", "mo", "bo"]

# TODO type your movie ratings tables here
# each row is a movie, each column is a student
movie_ratings = [
    [5, 9, 10],
    [4, 0, 5],
    [7, 7, 9], 
    [10, 5, 10],
    [5, 4, 7]
]

# TODO type your genre preferences table here
# each row is a student, each column is a genre
user_preferences = [
    [9, 4, 8, 6], 
    [10, 8, 4, 6],
    [6, 8, 8, 10]
]


your_ratings = np.zeros((5, 1))
# *** assuming you are the first column in the movie_ratings table ***
your_ratings[0] = movie_ratings[0][0] # rating for Back to the Future
your_ratings[1] = movie_ratings[1][0] # rating for Guardians of the Galaxy
your_ratings[2] = movie_ratings[2][0] # rating for Avatar
your_ratings[3] = movie_ratings[3][0] # rating for Trolls
your_ratings[4] = movie_ratings[4][0] # rating for Black Panther


# --- Normalization Process ---
# ratings, movies_features, and user_prefs are arrays which are more structured lists
ratings = np.array(movie_ratings)
movie_features = np.array(movie_genre)
user_prefs = np.array(user_preferences)

# append your ratings to the data representing everyone elses
ratings = np.append(your_ratings, ratings, axis=1)

# to check if a user has rated a movie, create a matrix that shows
# a 1 if the user rated it and a 0 if not
did_rate = (ratings != 0 ) * 1

# function to normalize the data
def normalize_ratings(ratings, did_rate):
    num_movies = ratings.shape[0]
    
    ratings_mean = np.zeros(shape = (num_movies, 1))
    ratings_norm = np.zeros(shape = ratings.shape)
    
    for i in range(num_movies): 
        # Get all the indexes where there is a 1
        idx = np.where(did_rate[i] == 1)[0]
        #  Calculate mean rating of ith movie only from user's that gave a rating
        ratings_mean[i] = np.mean(ratings[i, idx])
        ratings_norm[i, idx] = ratings[i, idx] - ratings_mean[i]
    
    return ratings_norm, ratings_mean

# use the fuction to get normalized data sets
ratings_norm, ratings_mean = normalize_ratings(ratings, did_rate)

# print the predictions in a nice way:
for index in range(len(movies)):
    # grab index (integer), which remember, are all sorted based on the prediction values 
    print("%.1f is predicted for the movie %s" % (ratings_mean[index], movies[index]))
