import webbrowser


class Movie():

    """A class to store movie related data and methods"""

    # constructor for movie instances
    def __init__(self, mov_title, mov_storyline, poster_img, trailer_youtube):
        self.title = mov_title
        self.storyline = mov_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

        # opens a browser and shows the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
