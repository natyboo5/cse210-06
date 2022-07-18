from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class FetchTitle(Actor):
    """A implement used to draw the title in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a title.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the title animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the title body.
        
        Returns:
            An instance of Body.
        """
        return self._body
