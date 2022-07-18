from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        bones = cast.get_actors(BONE_GROUP)
        for bone in bones:
            body_g = bone.get_body()
            position_g = body_g.get_position()
            x_g = position_g.get_x()
            y_g = position_g.get_y()

            if x_g < FIELD_LEFT:
                bone.bounce_x()
            elif x_g >= (FIELD_RIGHT - BONE_WIDTH):
                bone.bounce_x()

            if y_g > FIELD_BOTTOM:
                cast.remove_actor(BONE_GROUP, bone)