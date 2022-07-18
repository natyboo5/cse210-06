
from constants import *
from game.scripting.action import Action
from game.casting.sound import Sound
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point
from game.casting.background import Background


class DrawBonesAction(Action):

    def __init__(self, video_service, audio_service):
        self._audio_service = audio_service
        self._video_service = video_service
        self._bones_shown = []
        self._counter = 0
        self._bg_counter = 1

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

            order = bone.get_order()
            # velocity = body.get_velocity()

            if position.get_x() >= 100 and position.get_x() <= 150:
                if order not in self._bones_shown:
                    self._bones_shown.append(order)

                    self._counter += 1

                    print("*--------")
                    print(self._counter)
                    print()

                    if self._counter == 100:
                        sound = Sound(NEW_LEVEL_SOUND)
                        self._audio_service.play_sound(sound)
                        sound = Sound(GAME_SOUND)
                        self._audio_service.play_sound(sound)

                        stats = cast.get_first_actor(STATS_GROUP)
                        stats.next_level()
                        self._counter = 0

                        if self._bg_counter == 3:
                           self._bg_counter = 0

                        self._bg_counter += 1
                        self._add_background(cast, self._bg_counter)

            if position.get_x() == 1280:
                if order in self._bones_shown:
                    self._bones_shown.remove(order)

    def _add_background(self, cast, image_number):
        cast.clear_actors(BACKGROUND_GROUP)
        x = 0
        y = 0
        position = Point(x, y)
        size = Point(SCREEN_WIDTH, SCREEN_HEIGHT)
        body = Body(position, size)
        if image_number > 3:
            image_number = 3
        image_path = globals()[f"BACKGROUND_LEVEL{image_number}"]
        image = Image(image_path)
        background = Background(body, image, True)
        cast.add_actor(BACKGROUND_GROUP, background)
