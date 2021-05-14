from enum import Enum

from configs import MIN_THRESHOLD_FOR_CRITIC


class UserType(Enum):
    VIEWER = 1
    CRITIC = 2


class User:

    def __init__(self, name, user_type=UserType.VIEWER):
        self.name = name
        self.user_type = user_type
        self.ratings = []

    def add_rating(self, movie_rating):
        self.ratings.append(movie_rating)

        if self.total_ratings >= MIN_THRESHOLD_FOR_CRITIC:
            self.user_type = UserType.CRITIC

    @property
    def total_ratings(self):
        return len(self.ratings)
