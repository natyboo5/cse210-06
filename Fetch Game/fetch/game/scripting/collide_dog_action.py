from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideDogAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        pass
  