from constants import *
from game.scripting.action import Action


class DrawKeyboardAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        dog = cast.get_first_actor(KEYBOARD_GROUP)
        body = dog.get_body()

        if dog.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = dog.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)