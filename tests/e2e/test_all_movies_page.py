from flask.testing import FlaskClient
from app import app

def test_all_movies_page():
    testing_app = app.test_client()

    