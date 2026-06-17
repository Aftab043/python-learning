# WAP to ask the user to enter names of their 3 favorite movie & store them in a list.
# Create an empty list to store favorite movies
movie = []

# Take three favorite movie names from the user
movie1 = input("enter your 1st favorite movie :")
movie2 = input("enter your 2nd favorite movie :")
movie3 = input("enter your 3rd favorite movie :")

# Another way to create the list directly
# movie = [mov1,mov2,mov3]

# Add each movie to the list
movie.append(movie1)
movie.append(movie2)
movie.append(movie3)

# Print the final list of favorite movies
print(movie)

# Create another empty list for the same task
movie = []

# Take input from the user and add each movie directly to the list
movie.append(input("enter 1st movie name :"))
movie.append(input("enter 2st movie name :"))
movie.append(input("enter 3st movie name :"))

# Print the list of movies
print(movie)
