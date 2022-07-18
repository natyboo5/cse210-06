
from constants import *
from game.scripting.action import Action


class DrawBackgroundAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        background = cast.get_first_actor(BACKGROUND_GROUP)
        body = background.get_body()

        if background.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)

        image = background.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)