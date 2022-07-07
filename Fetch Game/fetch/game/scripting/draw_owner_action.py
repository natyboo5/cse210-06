from constants import *
from game.scripting.action import Action


class DrawOwnerAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        owner = cast.get_first_actor(OWNER_GROUP)
        body = owner.get_body()

        if owner.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = owner.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)