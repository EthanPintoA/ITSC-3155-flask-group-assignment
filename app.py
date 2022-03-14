from flask import Flask, redirect, render_template
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movies = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movieList=movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    return render_template('search_movies.html', search_active=True)
