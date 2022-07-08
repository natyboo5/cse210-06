from constants import *
from game.scripting.action import Action


class ChangeSceneAction(Action):

    def __init__(self, keyboard_service, next_scene, key):
        self._keyboard_service = keyboard_service
        self._next_scene = next_scene
        self._key = key
        
    def execute(self, cast, script, callback):
        if self._keyboard_service.is_key_pressed(self._key):
            callback.on_next(self._next_scene)