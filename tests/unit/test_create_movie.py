from src.models.movie import Movie
from src.repositories.movie_repository import MovieRepository


def test_create_movie():
    movie_repository = MovieRepository()

    movie0 = movie_repository.create_movie("Star Wars", "George Lucas", 5)
    movie1 = movie_repository.create_movie("Cats", "Tom Hooper", 1)
    movies = movie_repository.get_all_movies()

    assert len(movies) == 2

    assert movie0 == movies[0]
    assert movie1 == movies[1]

    assert type(movies[0]) == Movie
    assert movies[0].title == "Star Wars"
    assert movies[0].director == "George Lucas"
    assert movies[0].rating == 5

    assert type(movies[1]) == Movie
    assert movies[1].title == "Cats"
    assert movies[1].director == "Tom Hooper"
    assert movies[1].rating == 1
