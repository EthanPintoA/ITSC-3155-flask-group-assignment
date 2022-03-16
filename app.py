
from flask import Flask, abort, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    title = request.form.get("title", "")
    director = request.form.get("director", "")
    rating = request.form.get("rating", "")

    if (
        "" in (title, director, rating) or
        not (rating.isdecimal() and 1 <= int(rating) <= 5)
    ):
        abort(400)
    movie_repository_singleton.create_movie(title, director, int(rating))
    return redirect('/movies')


@app.get('/movies/search')  # Route to the Search Movies form
def search_movies():
    input_movie = request.args.get('input_movie', 'Error: No Parameter')
    if input_movie == 'Error: No Parameter':
        search_movie = 'Error: No Parameter'
    else:
        search_movie = movie_repository_singleton.get_movie_by_title(
            input_movie)
    return render_template('search_movies.html', input_movie=input_movie, search_movie=search_movie, search_active=True)
