from builtins import Exception


class MovieNotReleased(Exception):
    def __init__(self, movie_name):
        self.movie_name = movie_name
        super().__init__()

    def __str__(self):
        return ""


class MovieAlreadyReviewed(Exception):
    def __init__(self, movie_name, user_name):
        self.movie_name = movie_name
        self.user_name = user_name
        super().__init__()

    def __str__(self):
        return ""
