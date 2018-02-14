import webbrowser
"""
This Webbrowser is a module in python which opens
the webborwser directly. Its cis written on the
backend. Here we are importing this library.
"""


"""
Below is the class Movie(). Inside this class
we have written the code for calling the movie
attributes in the entertainment_center.py file.
Here inside this function we have created two new
functions which are used as a call back to bring
needed info from the other files.
"""


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
