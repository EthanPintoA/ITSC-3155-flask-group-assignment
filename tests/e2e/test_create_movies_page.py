from flask.testing import FlaskClient


def test_create_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data

    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response_data

    assert b'<form action="/movies" method="post">' in response_data

    assert b'<input type="text" class="form-control mb-3" name="title" id="title" />' in response_data

    assert b'<input type="text" class="form-control mb-3" name="director" id="director" />' in response_data

    assert b'<select class="form-control mb-3" name="rating" id="rating">' in response_data
    assert b'<option value="5">&#9733 &#9733 &#9733 &#9733 &#9733</option>' in response_data
    assert b'<option value="4">&#9733 &#9733 &#9733 &#9733</option>' in response_data
    assert b'<option value="3">&#9733 &#9733 &#9733</option>' in response_data
    assert b'<option value="2">&#9733 &#9733</option>' in response_data
    assert b'<option value="1">&#9733</option>' in response_data

    assert b'<button type="submit" class="btn btn-primary mb-3">Submit</button>' in response_data
