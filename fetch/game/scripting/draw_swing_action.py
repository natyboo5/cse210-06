from constants import *
from game.scripting.action import Action


class DrawSwingAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        swing = cast.get_first_actor(SWING_GROUP)
        body = swing.get_body()

        if swing.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = swing.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)