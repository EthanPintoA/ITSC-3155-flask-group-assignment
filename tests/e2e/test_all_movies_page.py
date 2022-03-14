from flask import Flask
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton
from app import app
import pytest

@pytest.fixture
def testing_app():
    return app.test_client()

def test_all_movies_page(testing_app: FlaskClient):
    
    movie_repository_singleton.create_movie("Batman", "Caden", 4)
    movie_repository_singleton.create_movie("Superman", "William", 5)
    movie_repository_singleton.create_movie("Hulk", "Josh", 3)

    response = testing_app.get('/movies')
    
    assert b"<td>Batman</td>" in response.data
    assert b"<td>Caden</td>" in response.data
    assert b"<td>4</td>" in response.data

    assert b"<td>Superman</td>" in response.data
    assert b"<td>William</td>" in response.data
    assert b"<td>5</td>" in response.data

    assert b"<td>Hulk</td>" in response.data
    assert b"<td>Josh</td>" in response.data
    assert b"<td>3</td>" in response.data