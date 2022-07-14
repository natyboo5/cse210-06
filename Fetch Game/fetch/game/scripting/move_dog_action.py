from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveDogAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        dog = cast.get_first_actor(DOG_GROUP)
        body = dog.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        position = position.add(velocity)

        if x < SCREEN_WIDTH / 3:
            position = Point(SCREEN_WIDTH / 3, y)
        elif x > (SCREEN_WIDTH - DOG_WIDTH):
            position = Point(SCREEN_WIDTH - DOG_WIDTH, y)

        if y < 0:
            position = Point(x, 0)
        elif y > (SCREEN_HEIGHT - DOG_HEIGHT):
            position = Point(x, SCREEN_HEIGHT - DOG_HEIGHT)

        body.set_position(position)
