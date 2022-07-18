
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.image import Image
from game.casting.animation import Animation



class BoneHelp(Actor):
    """A solid, object that is draw in the help menu."""

    def __init__(self, body, type_of_bone=0, debug = False):
        """Constructs a new Bone.

        Args:
            animation: A new instance of Animation.
            body: A new instance of Body.
            type_of_bone: It's the type of the bone.
        """
        super().__init__(debug)
        self._animation = 0
        self._body = body

        self._type_of_bone = type_of_bone
        # BONE
        if type_of_bone == 2:
            self._animation = Animation(BONE_IMAGES, RATE_ITEMS_HELP)
        # BONE WITH MEAT
        elif type_of_bone == 1:
            self._animation = Animation(BONE_MEAT_IMAGES, RATE_ITEMS_HELP)
        # DYNAMITE
        elif type_of_bone == 3:
            self._animation = Animation(DYNAMITE_IMAGE, RATE_ITEMS_HELP)

        # LIVES
        elif type_of_bone == 0:
            self._animation = Animation(HEART_IMAGES, RATE_ITEMS_HELP)



    def get_animation(self):
        """Gets the items's animation.

        Returns:
            An instance of Animation.
        """
        return self._animation



    def get_body(self):
        """Gets the bone's body.

        Returns:
            An instance of Body.
        """
        return self._body

   
