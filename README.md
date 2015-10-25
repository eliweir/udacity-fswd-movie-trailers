# Movies Trailer Website

Basic movie trailer website created with Python, in partial fulfilment of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004). The `generate_html.py` module is a edit of the `fresh_tomatoes.py` file  [provided in the courseware](https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py). All other work original, no attribution necessary.

## Modules

1. movie_trailers_website.py - the core module, that imports others as needed. Creates a list of movies then passes the list to an HTML generator module to output static content.
2. media.py - used by `movie_trailers_website.py` to instantiate movies.
3. generate_html.py - used by `movie_trailers_website.py` to generate static HTML page from a list of movies.

##Usage
To use, simply run `movie_trailers_website.py`. This will generate an `index.html` file which will then be displayed. If the `index.html` file already exists it will be overwritten. The `index.html` file can also be viewed directly.

If you wish, the list of movies can be edited (e.g. movies added, removed, and properties such as description changed) in the `movie_trailers_website.py` module.

**Movie properties**

Movies have the following properties, which are all strings:
- `title` The movie title
- `year` Year the movie was released
- `director` The movie director
- `storyline` Brief summary of the plot
- `cast` Main actors
- `image_url` URL of a poster image
- `trailer_url` URL of a YouTube video
- `rating` Number of stars out of 5

**Example**

Here is an example of creating an instance for Toy Story, which can then be added to the list of movies to be displayed:

```python
toy_story = media.Movie("Toy Story",
                        "1995",
                        "John Lasseter",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "Tom Hanks, Tim Allen, Don Rickles",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "4.5")

movie_list = [movie1, movie2, toy_story]
```
