
from constants import *
from game.scripting.action import Action


class DrawBonesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        # self._bones_shown = []
        self._counter = 0

    def execute(self, cast, script, callback):
        bones = cast.get_actors(BONE_GROUP)

        for bone in bones:
            body = bone.get_body()

            if bone.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)

            image = bone.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)

            order = bone.get_order()
            # velocity = body.get_velocity()

            if position.get_x() == 10:
                # if order not in self._bones_shown:
                    # self._bones_shown.append(order)

                self._counter += 1

                print("*--------")
                print(self._counter)
                print()

                if self._counter == 100:
                    stats = cast.get_first_actor(STATS_GROUP)
                    stats.next_level()
                    self._counter = 0
