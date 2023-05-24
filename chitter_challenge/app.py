from playwright.sync_api import Page, expect
import time
import re
from lib.peep_repository import *
from lib.user_repository import *
from lib.user import *
from lib.peep import *
import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection



# Create a new Flask app
app = Flask(__name__)


@app.route('/peeps', methods=['GET'])
def get_peeps_formatted():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps, usernames = repository.all()
    user_repo = UserRepository(connection)
    users = user_repo.all()
    return render_template("chitterpeeps/index.html", peeps=peeps, usernames=usernames, users=users)

@app.route('/peeps', methods=['POST'])
def create_peep():
    connection = get_flask_database_connection(app)
    repo = PeepRepository(connection)
    message = request.form['peep']
    user = request.form['user']
    user_repo = UserRepository(connection)
    user_object = user_repo.find_by_username(user)
    peep = Peep(None, message, None, user_object.id )
    repo.create(peep)
    return redirect(url_for('get_peeps_formatted'))

@app.route('/peeps/new', methods=['GET'])
def get_user_form():
    return render_template("chitterpeeps/new_user_form.html")

@app.route('/peeps/new', methods=['POST'])
def create_new_user():
    print("function calledp")
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    actualname = request.form['actualname']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    user = User(None, actualname, username, password, email)
    result = repo.create(user)
    if result == "username already taken":
        user_error = True
        return render_template('chitterpeeps/new_user_form.html', username_error=user_error)
    if result == "email already has account":
        email_error = True
        return render_template('chitterpeeps/new_user_form.html', email_error=email_error)
    return redirect(url_for('get_peeps_formatted'))









# @app.route('/albums', methods=['POST'])
# def create_album():
#         # Set up the database connection and repository
#         connection = get_flask_database_connection(app)
#         repository = AlbumRepository(connection)
#         # Get the fields from the request form
#         title = request.form['title']
#         release_year = request.form['release_year']
#         # Create a book object
#         album = Album(None, title, release_year, 1)
#         # # Check for validity and if not valid, show the form again with errors
#         if not album.is_valid():
#             return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400

#         # Save the book to the database
#         album = repository.create(album)

#         # Redirect to the book's show route to the user can see it
#         return redirect(f"/albums/{album.id}")
# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji

# def has_no_parameters_artist(form):
#     return ('artist_name' not in form) or ('genre' not in form)

# def has_no_parameters_album(form):
#     return ('title' not in form) or ('release_year' not in form) or ('artist_id' not in form) 


# @app.route('/albums', methods=['POST'])
# def post_albums():
#     if has_no_parameters_album(request.form):
#         return "You need to submit a title, release_year and artist id", 400
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
#     repository.create(album)
#     return '', 200

# # @app.route('/albums', methods=['GET'])
# # def get_albums():
# #     connection = get_flask_database_connection(app)
# #     repository = AlbumRepository(connection)
# #     return "\n".join(
# #         f"{album}" for album in repository.all() 
# #     )

# @app.route('/albums')
# def get_albums_formatted():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     albums = repository.all()
#     print("albums", albums)
#     return render_template(
#         "albums/index.html", albums=albums 
#     )
# @app.route('/artists')
# def get_artists_formatted():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all()
#     return render_template("artists/index.html", artists=artists)


# @app.route('/albums/<int:album_id>')
# def get_single_album_formatted(album_id):
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = repository.find(album_id)
#     print("this is album", album)
#     return render_template(
#         "albums/show.html", album=album
#     )

# @app.route('/artists/<int:artist_id>')
# def get_single_artist_formatted(artist_id):
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist = repository.find(artist_id)
#     return render_template("artists/show.html", artist=artist)

# @app.route('/artists/new', methods=['GET'])
# def get_new_artist():
#     return render_template('artists/new.html')

# @app.route('/albums', methods=['POST'])
# def create_album():
#         # Set up the database connection and repository
#         connection = get_flask_database_connection(app)
#         repository = AlbumRepository(connection)
#         # Get the fields from the request form
#         title = request.form['title']
#         release_year = request.form['release_year']
#         # Create a book object
#         album = Album(None, title, release_year, 1)
#         # # Check for validity and if not valid, show the form again with errors
#         if not album.is_valid():
#             return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400

#         # Save the book to the database
#         album = repository.create(album)

#         # Redirect to the book's show route to the user can see it
#         return redirect(f"/albums/{album.id}")


# @app.route('/artists', methods=['POST'])
# def create_artist():
#         # Set up the database connection and repository
#         connection = get_flask_database_connection(app)
#         repository = ArtistRepository(connection)

#         # Get the fields from the request form
#         name = request.form['artist_name']
#         genre = request.form['genre']

#         artist = Artist(None, name, genre)

#         # # # Check for validity and if not valid, show the form again with errors
#         if not artist.is_valid():
#             return render_template('artists/new.html', artist=artist, errors=artist.generate_errors()), 400
#         # Save the book to the database
#         artist = repository.create(artist)
#         # # Redirect to the book's show route to the user can see it
#         return redirect(f"/artists/{artist.id}")

    # GET /books/new
    # Returns a form to create a new book
# @app.route('/albums/new', methods=['GET'])
# def get_new_album():
#     return render_template('albums/new.html')



# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
