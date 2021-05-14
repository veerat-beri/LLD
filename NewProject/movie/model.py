
from user.model import User


class Movie:
    def __init__(self, release_year, name, genre):
        self.release_year = release_year
        self.name = name
        self.genre = genre

    def __str__(self):
        return f"{self.name}: {self.release_year}: {self.genre}"




class MovieRating:
    def __init__(self, movie: Movie, review_by: User, rating):
        self.movie = movie
        self.review_by = review_by
        self.rating = rating



