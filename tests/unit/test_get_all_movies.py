from pytest import fail
from src.models.movie import Movie
from src.repositories.movie_repository import MovieRepository

def test_get_all_movies():
    movie_repo = MovieRepository()

    movie_repo.create_movie("Batman", "Caden", 4)
    movie_repo.create_movie("Superman", "William", 5)
    movie_repo.create_movie("Hulk", "Josh", 3)

    assert movie_repo.get_all_movies()[0].title == "Batman"
    assert movie_repo.get_all_movies()[0].director == "Caden"
    assert movie_repo.get_all_movies()[0].rating == 4

    assert movie_repo.get_all_movies()[1].title == "Superman"
    assert movie_repo.get_all_movies()[1].director == "William"
    assert movie_repo.get_all_movies()[1].rating == 5

    assert movie_repo.get_all_movies()[2].title == "Hulk"
    assert movie_repo.get_all_movies()[2].director == "Josh"
    assert movie_repo.get_all_movies()[2].rating == 3

    try: 
        movie_repo.get_all_movies()[3]
        assert False
    except IndexError:
        assert True