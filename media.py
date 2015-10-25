# Used by movie_trailers_website.py to instantiate movie objects

# Dependencies
import webbrowser

# Contains movie data
class Movie():

    def __init__(self, movie_title, movie_year, movie_director, movie_storyline, movie_cast, movie_image_url, movie_trailer_url, movie_rating):
        self.title = movie_title
        self.year = movie_year
        self.director = movie_director
        self.storyline = movie_storyline
        self.cast = movie_cast
        self.image_url = movie_image_url
        self.trailer_url = movie_trailer_url
        self.rating = movie_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
