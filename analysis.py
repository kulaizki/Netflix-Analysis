# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies[netflix_movies.duration < 60]

# Define an empty list
colors = []

for l, r in netflix_movies.iterrows() :
    if r["genre"] == "Children" :
        colors.append("red")
    elif r["genre"] == "Documentaries" :
        colors.append("blue")
    elif r["genre"] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")
           
colors[:10]

fig = plt.figure(figsize=(12,8))

plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)

plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
answer = "maybe"