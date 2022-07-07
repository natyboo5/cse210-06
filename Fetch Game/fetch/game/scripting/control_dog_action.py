from constants import *
from game.scripting.action import Action


class ControlDogAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        dog = cast.get_first_actor(DOG_GROUP)
        if self._keyboard_service.is_key_down(UP): 
            dog.swing_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            dog.swing_down() 
        elif self._keyboard_service.is_key_down(LEFT): 
            dog.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            dog.swing_right()  
        else: 
            dog.stop_moving()        