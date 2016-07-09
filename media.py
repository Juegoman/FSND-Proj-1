import webbrowser
class Anime():
    """A class to model an anime."""
    # Constructor, takes in the title, the synopsis, a poster type image, and a
    # YouTube link to the opening theme of the show.
    def __init__(this, anime_title, anime_synopsis, image, op_yt):
        this.title = anime_title
        this.synopsis = anime_synopsis
        this.image_url = image
        this.op_yt_url = op_yt
