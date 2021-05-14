from collections import defaultdict
from datetime import datetime

from movie.exceptions import MovieAlreadyReviewed, MovieNotReleased
from movie.model import Movie, MovieRating
from user.model import User, UserType

movie_viewer_score = defaultdict(float)
movie_critic_score = defaultdict(float)
movies_reviewed = {}


class MovieReview:

    # @property
    # def movie_viewer_score(self):
    #     global __movie_viewer_score
    #     return __movie_viewer_score
    #
    # @property
    # def movie_critic_score(self):
    #     global __movie_critic_score
    #     return __movie_critic_score
    #
    # def _update_movie_critic_score(self, movie_name, rating):
    #     global __movie_critic_score
    #     __movie_critic_score[movie_name] += rating
    #
    # def _update_movie_viewer_score(self, movie_name, rating):
    #     global __movie_viewer_score
    #     __movie_viewer_score[movie_name] += rating

    def add_review(self, movie: Movie, reviewed_by: User, rating):
        if movie.release_year > 2021:
            raise MovieNotReleased(movie.name)

        if movies_reviewed.get(movie.name) and movies_reviewed.get(movie.name).get(reviewed_by.name):
            raise MovieAlreadyReviewed(movie.name, reviewed_by.name)

        if not movies_reviewed.get(movie.name):
            movies_reviewed[movie.name] = {}
            movie_rating = MovieRating(movie, reviewed_by, rating)
            movies_reviewed[movie.name][reviewed_by.name] = movie_rating
            reviewed_by.add_rating(movie_rating)

        movies_reviewed[movie.name][reviewed_by.name] = movie_rating
        self.update_movie_score(movie_rating)

    def update_movie_score(self, movie_rating: MovieRating):
        if movie_rating.review_by.user_type == UserType.CRITIC:
            rating = movie_rating.rating * 2
            movie_critic_score[movie_rating.movie.name] = movie_critic_score[movie_rating.movie.name] + rating

        else:
            rating = movie_rating.rating
            movie_viewer_score[movie_rating.movie.name] = movie_viewer_score[movie_rating.movie.name] + rating

    def get_top_n_movies_by_name(self, n, user_type=UserType.VIEWER, movies_by_year=[], movies_by_genre=[]):
        search_map = movie_viewer_score if user_type == UserType.VIEWER else movie_critic_score
        movies_to_check = []
        filtered_ratings = {}

        if movies_by_year:
            print(movies_by_year)
            movies_to_check = [movie.name for movie in movies_by_year[0]]

        if movies_by_genre:
            movies_to_check = [movie.name for movie in movies_by_genre]

        for movie_name in movies_to_check:
            if search_map.get(movie_name):
                filtered_ratings[movie_name] = search_map[movie_name]
        return [movie_name for movie_name, _ in sorted(filtered_ratings, key=lambda pair: (pair[1], pair[0]))[:n]]
