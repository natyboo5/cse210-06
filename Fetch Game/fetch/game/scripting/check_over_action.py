from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bones = cast.get_actors(BONE_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        if len(bones) == 0 or stats.get_lives() == 0:
            callback.on_next(GAME_OVER)

        
        # if len(bones) == 0:
        #     callback.on_next(TRY_AGAIN)
        #     stats.next_level()
        #     callback.on_next(NEXT_LEVEL)