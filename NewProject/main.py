

# Driver Code
from movie.catalogue import MovieCatalogue
from service.movie_services import MovieReview
from user.services import add_user, users


def run():
    movie_review = MovieReview()
    MovieCatalogue.add_movie("Don", 2006, ["Comedy", "Action"])
    add_user("SRK")

    user = users.get("SRK")
    movie = MovieCatalogue.search_by_name("Don")
    print("movie: ", movie)

    movie_review.add_review(movie, user, 2)
    print(movie_review.get_top_n_movies_by_name(1, movies_by_year=[MovieCatalogue.search_by_year(2006)]))




if __name__ == '__main__':
    run()

