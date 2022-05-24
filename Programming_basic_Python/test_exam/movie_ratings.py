import sys

count_movies = int(input())
max_rating = - sys.maxsize
min_rating = sys.maxsize
total_rating = 0
movie_min_rate = ''
movie_max_rate = ''
for movie in range(count_movies):
    name = input()
    rating = float(input())
    total_rating += rating
    if rating > max_rating:
        max_rating = rating
        movie_max_rate = name
    if rating < min_rating:
        min_rating = rating
        movie_min_rate = name
average_rating = total_rating / count_movies
print(f"{movie_max_rate} is with highest rating: {max_rating:.1f}")
print(f"{movie_min_rate} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
