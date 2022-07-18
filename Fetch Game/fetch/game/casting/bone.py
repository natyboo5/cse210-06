
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.image import Image
from game.casting.animation import Animation



class Bone(Actor):
    """A solid, object that move around in the game."""

    def __init__(self, body, order, type_of_bone=0, debug = False):
        """Constructs a new Bone.

        Args:
            body: A new instance of Body.
            order: Bone order.
            type_of_bone: It's the type of the bone.
            animation: A new instance of Animation.
        """
        super().__init__(debug)
        self._image = 0
        self._animation = 0
        self._body = body
        self._order = order

        self._type_of_bone = type_of_bone
        # BONE
        if type_of_bone == 0:
            self._animation = Animation(BONE_IMAGES, RATE_ITEMS)
            self.set_points(BONE_POINTS)
        # BONE WITH MEAT
        elif type_of_bone == 1:
            self._animation = Animation(BONE_MEAT_IMAGES, RATE_ITEMS)
            self.set_points(BONE_MEAT_POINTS)
        # DYNAMITE
        elif type_of_bone == 2:
            self._animation = Animation(DYNAMITE_IMAGE, RATE_ITEMS)
            self.set_points(DYNAMITE_POINTS)

        # LIVES
        elif type_of_bone == 3:
            self._animation = Animation(HEART_IMAGES, RATE_ITEMS)
            self.set_points(HEART_POINTS)



    def get_animation(self):
        """Gets the items's animation.

        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_type(self):
        return self._type_of_bone

    def get_body(self):
        """Gets the bone's body.

        Returns:
            An instance of Body.
        """
        return self._body

    def get_order(self):
        """Gets the bone's order.

        Returns:
            An instance of Body.
        """
        return self._order

    def get_points(self):
        """Gets the bone's points.

        Returns:
            A number representing the bone's points.
        """
        return self._points


    def get_image(self):
        """Gets the bone's image.

        Returns:
            An instance of Image.
        """
        return self._image


    def bounce_x(self):
        """Bounces the BONE in the X direction."""
        velocity = self._body.get_velocity()
        vx = velocity.get_x()
        vy = velocity.get_y() * -1
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
