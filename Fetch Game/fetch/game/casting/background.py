
from constants import *
from game.casting.actor import Actor


class Background(Actor):
    """Background."""

    def __init__(self, body, animation, debug=False):
        """Constructs a new Background.

        Args:
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._animation = animation
        self._body = body
        

    def get_animation(self):
        """Gets the background's animation.

        Returns:
            An instance of animation.
        """
        return self._animation

    def get_body(self):
        """Gets the background's body.

        Returns:
            An instance of Body.
        """
        return self._body
