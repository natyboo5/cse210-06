from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class HeartWin(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new owner.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the owner's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the owner's body.
        
        Returns:
            An instance of Body.
        """
        return self._body
