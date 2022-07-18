from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Dog(Actor):
    """A implement used to draw the dog in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new dog.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the dog's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the dog's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the dog using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_up(self):
        """Steers the dog up."""
        velocity = Point(0, -DOG_VELOCITY)
        self._body.set_velocity(velocity)
        
    def swing_down(self):
        """Steers the dog down."""
        velocity = Point(0, DOG_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_left(self):
        """Steers the dog to the left."""
        velocity = Point(-DOG_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the dog to the right."""
        velocity = Point(DOG_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the dog from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)