# MOVIE TRAILERS
# Eli Weir 24/10/2015
# Programming Foundations with Python
# (for Udacity Fullstack Nanodegree)


# Dependencies
import media
import output_html


# Create movie instances
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
dope = media.Movie("Dope", "A 90's hip-hop obsessed geek surviving life in a tough neighborhood", "https://upload.wikimedia.org/wikipedia/en/d/d2/DopeTeaserPoster.jpg", "https://www.youtube.com/watch?v=strEm9amZuo")
straight_outta_compton = media.Movie("Straight Outta Compton", "The story of the world's most influential and contraversial hip-hop group", "https://upload.wikimedia.org/wikipedia/en/7/7a/Straight_Outta_Compton_poster.jpg", "https://www.youtube.com/watch?v=fKaisid1jz8")
southpaw = media.Movie("Southpaw", "A tortured boxer's journey to redemption, for his daughter", "https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg", "https://www.youtube.com/watch?v=Mh2ebPxhoLs")
cartel_land = media.Movie("Cartel Land", "Hard-hitting documentary follows anti-cartel vigilante groups on both side of the border", "https://upload.wikimedia.org/wikipedia/en/2/21/Cartel_Land_poster.jpg", "www.youtube.com/watch?v=6JD7hPM_yxg")

# Make a list of my movies
movies = [toy_story, avatar, dope, straight_outta_compton, southpaw, cartel_land]

# Show movie page
output_html.open_movies_page(movies)
