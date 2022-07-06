from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        position = position.add(velocity)

        if x < 0:
            position = Point(0, y)
        elif x > (SCREEN_WIDTH - RACKET_WIDTH):
            position = Point(SCREEN_WIDTH - RACKET_WIDTH, y)
            
        if y < 0:
            position = Point(x, 0)
        elif y > (SCREEN_HEIGHT - RACKET_HEIGHT):
            position = Point(x, SCREEN_HEIGHT - RACKET_HEIGHT)

        body.set_position(position)
        