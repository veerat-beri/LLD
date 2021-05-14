from collections import defaultdict
from email.policy import default

# from movie.interfaces import SearchByYear, SearchByGenre
from movie.model import Movie

movies_by_year = defaultdict(list)
movies_by_name = {}
movies_by_genre = defaultdict(list)


# class MovieCatalogue(SearchByYear, SearchByGenre):
class MovieCatalogue:
    @staticmethod
    def search_by_year(year):
        return movies_by_year.get(year)

    @staticmethod
    def search_by_genre(genre):
        # handle multiple
        return movies_by_genre.get(genre)

    @staticmethod
    def search_by_name(name):
        return movies_by_name.get(name)

    @staticmethod
    def add_movie(name, release_year, genres: []):

        for genre in genres:
            movie_obj = Movie(release_year, name, genre)
            movies_by_year[release_year].append(movie_obj)
            movies_by_genre[genre].append(movie_obj)
            movies_by_name[name] = movie_obj
            print("Movie added: ", movie_obj)



