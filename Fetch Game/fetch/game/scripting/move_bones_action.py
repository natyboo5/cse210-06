
from constants import *
from game.scripting.action import Action


class MoveBonesAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        bones = cast.get_actors(BONE_GROUP)

        for bone in bones:
            body = bone.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)