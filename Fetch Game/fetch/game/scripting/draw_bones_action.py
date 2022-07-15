
from constants import *
from game.scripting.action import Action


class DrawBonesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bones = cast.get_actors(BONE_GROUP)

        for bone in bones:
            body = bone.get_body()

            if bone.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)

            animation = bone.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)