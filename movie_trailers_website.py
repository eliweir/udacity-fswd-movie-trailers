# MOVIE TRAILERS WEBSITE
# Eli Weir 25/10/2015
# Programming Foundations with Python
# (for Udacity Fullstack Nanodegree)

# Main module, that imports others as needed.
# Creates list of movies, then passes the list to an HTML generator module to output static content.


# Dependencies
import media
import generate_html


# Create movie instances
toy_story = media.Movie("Toy Story",
                        "1995",
                        "John Lasseter",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "Tom Hanks, Tim Allen, Don Rickles",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "4.5")
avatar = media.Movie("Avatar",
                     "2009",
                     "James Cameron",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "4")
dope = media.Movie("Dope",
                   "2015",
                   "Rick Famuyiwa",
                   "A 90's hip-hop obsessed geek survives life in a tough neighborhood",
                   " Shameik Moore, Tony Revolori, Kiersey Clemons",
                   "https://upload.wikimedia.org/wikipedia/en/d/d2/DopeTeaserPoster.jpg",
                   "https://www.youtube.com/watch?v=strEm9amZuo",
                   "4")
straight_outta_compton = media.Movie("Straight Outta Compton",
                                     "2015",
                                     "F. Gary Gary",
                                     "The story of the world's most influential and contraversial hip-hop group",
                                     " O'Shea Jackson Jr., Corey Hawkins, Jason Mitchell",
                                     "https://upload.wikimedia.org/wikipedia/en/7/7a/Straight_Outta_Compton_poster.jpg",
                                     "https://www.youtube.com/watch?v=fKaisid1jz8",
                                     "4.5")
southpaw = media.Movie("Southpaw",
                       "2015",
                       "Antoine Fuqua",
                       "A tortured boxer's journey to redemption, for his daughter",
                       " Jake Gyllenhaal, Rachel McAdams, Oona Laurence",
                       "https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg",
                       "https://www.youtube.com/watch?v=Mh2ebPxhoLs",
                       "3.5")
cartel_land = media.Movie("Cartel Land",
                          "2015",
                          "Matthew Heineman",
                          "Hard-hitting documentary follows anti-cartel vigilante groups on both side of the border",
                          "Robert Hetrick",
                          "https://upload.wikimedia.org/wikipedia/en/2/21/Cartel_Land_poster.jpg",
                          "www.youtube.com/watch?v=6JD7hPM_yxg",
                          "4")


# Create a list of the movies
movie_list = [toy_story, avatar, dope, straight_outta_compton, southpaw, cartel_land]


# Generate and display HTML movie page, using the list of movies
generate_html.open_movies_page(movie_list)
