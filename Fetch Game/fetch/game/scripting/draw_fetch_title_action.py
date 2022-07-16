from constants import *
from game.scripting.action import Action


class DrawFetchTitleAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        fetch_title = cast.get_first_actor(FETCH_TITLE_GROUP)
        body = fetch_title.get_body()

        if fetch_title.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = fetch_title.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)