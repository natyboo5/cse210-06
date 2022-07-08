
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Background(Actor):
    """Background."""

    def __init__(self, body, image, debug=False):
        """Constructs a new Background.

        Args:
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._image = image
        self._body = body
        self._position = Point(0, 0)

    def get_image(self):
        """Gets the owner's image.

        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the owner's body.

        Returns:
            An instance of Body.
        """
        return self._body
