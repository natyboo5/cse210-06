
from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBoneAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        dog = cast.get_first_actor(DOG_GROUP)
        bones = cast.get_actors(BONE_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for bone in bones:
            dog_body = dog.get_body()
            bone_body = bone.get_body()

            if self._physics_service.has_collided(dog_body, bone_body):
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = bone.get_points()
                stats.add_points(points)

                # DYNAMITE
                if bone.get_type() == 2:  
                    stats.lose_life()
                
                # HEART
                if bone.get_type() == 3:  
                    stats.add_life()

                cast.remove_actor(BONE_GROUP, bone)
