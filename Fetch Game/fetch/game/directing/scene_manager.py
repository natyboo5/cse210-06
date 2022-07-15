import csv
import random
from constants import *
from game.casting.animation import Animation
from game.casting.bone import Bone
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.dog import Dog
from game.casting.dog_sad import DogSad
from game.casting.owner import Owner
from game.casting.stats import Stats
from game.casting.text import Text
from game.casting.background import Background
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_dog_action import CollideDogAction
from game.scripting.collide_bone_action import CollideBoneAction
from game.scripting.control_dog_action import ControlDogAction
from game.scripting.draw_bones_action import DrawBonesAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_dog_action import DrawDogAction
from game.scripting.draw_dog_sad_action import DrawDogSadAction
from game.scripting.draw_owner_action import DrawOwnerAction
from game.scripting.draw_background_action import DrawBackgroundAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_bones_action import MoveBonesAction
from game.scripting.move_dog_action import MoveDogAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(
        PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_DOG_ACTION = CollideDogAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_DOG_ACTION = CollideBoneAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BONES_ACTION = CollideBoneAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_DOG_ACTION = ControlDogAction(KEYBOARD_SERVICE)
    DRAW_BONES_ACTION = DrawBonesAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_DOG_ACTION = DrawDogAction(VIDEO_SERVICE)
    DRAW_DOG_SAD_ACTION = DrawDogSadAction(VIDEO_SERVICE)
    DRAW_OWNER_ACTION = DrawOwnerAction(VIDEO_SERVICE)
    DRAW_BACKGROUND_ACTION = DrawBackgroundAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(
        AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BONES_ACTION = MoveBonesAction()
    MOVE_DOG_ACTION = MoveDogAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == FIRST_MENU:
            self._prepare_help(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:
            self._prepare_game_over(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game(self, cast, script):

        cast.clear_actors(DIALOG_GROUP)

        self._add_dialog(cast, GAME_NAME, FONT,
                         FONT_SIZE_TITLE, ALIGN_CENTER, Point(CENTER_X, 200))
        self._add_dialog(cast, ENTER_TO_START, FONT, FONT_LARGE,
                         ALIGN_CENTER, Point(CENTER_X, CENTER_Y), True)
        self._add_dialog(cast, SHOW_INSTRUCTIONS, FONT, FONT_LARGE,
                         ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 100), True)
        self._add_dialog(cast, FIRST_MENU_INSTRUCTIONS, FONT, FONT_LARGE,
                         ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 200), True)

        self._add_background(cast, BACKGROUND_FIRST_MENU)

        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEXT_LEVEL, ENTER))
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, FIRST_MENU, HELP))

        self._add_initialize_script(script)
        self._add_load_script(script)

        draw = [
            self.DRAW_BACKGROUND_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, draw)

        self._add_unload_script(script)
        self._add_release_script(script)

        script.add_action(OUTPUT, PlaySoundAction(
            self.AUDIO_SERVICE, WELCOME_SOUND))

    def _prepare_help(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        self._add_dialog(cast, BONE_INSTRUCTIONS, FONT,
                         FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, CENTER_Y), True)
        self._add_dialog(cast, BONE_MEAT_INSTRUCTIONS, FONT,
                         FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 100), True)
        self._add_dialog(cast, DYNAMITE_INSTRUCTIONS, FONT,
                         FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 200), True)

        # MENU
        self._add_dialog(cast, FIRST_MENU_INSTRUCTIONS, FONT, FONT_LARGE,
                         ALIGN_CENTER, Point(CENTER_X, 200), True)

        self._add_background(cast, BACKGROUND)

        # MOVE TO OTHERS SCENES
        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEW_GAME, MENU))

        draw = [
            self.DRAW_BACKGROUND_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, draw)

        script.add_action(OUTPUT, PlaySoundAction(
            self.AUDIO_SERVICE, WELCOME_SOUND))

    def _prepare_next_level(self, cast, script):
        self._add_stats(cast)

        self._add_level(cast)

        self._add_lives(cast)
        self._add_score(cast)
        self._add_bones(cast)
        self._add_dog(cast)
        self._add_owner(cast)

        self._add_background(cast, BACKGROUND_LEVEL1)

        self._add_dialog(cast, PREP_TO_LAUNCH, FONT, FONT_SMALL,
                         ALIGN_CENTER, Point(CENTER_X, CENTER_Y))

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))

        draw = [
            self.DRAW_BACKGROUND_ACTION,
            self.DRAW_HUD_ACTION,
            self.DRAW_BONES_ACTION,
            self.DRAW_OWNER_ACTION,
            self.DRAW_DOG_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, draw)

        script.add_action(OUTPUT, PlaySoundAction(
            self.AUDIO_SERVICE, GAME_SOUND))

    def _prepare_try_again(self, cast, script):
        # self._add_bones(cast)
        # self._add_dog(cast)
        # self._add_owner(cast)

        self._add_dialog(cast, WAS_GOOD_GAME, FONT,
                         FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, CENTER_Y))

        self._add_background(cast, BACKGROUND_LEVEL1)

        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)

        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))

        # self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_DOG_ACTION)
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEXT_LEVEL, RESTART))
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEW_GAME, MENU))
        self._add_update_script(script)

        draw = [
            self.DRAW_BACKGROUND_ACTION,
            self.DRAW_HUD_ACTION,
            self.DRAW_BONES_ACTION,
            self.DRAW_OWNER_ACTION,
            self.DRAW_DOG_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, draw)

    def _prepare_game_over(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        self._add_dialog(cast, WAS_GOOD_GAME, FONT,
                         FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, 100))
        self._add_dialog(cast, "FINAL SCORE  " + str(stats.get_score()),
                         FONT, FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 200), True)
        self._add_dialog(cast, FIRST_MENU_INSTRUCTIONS, FONT, FONT_SMALL,
                         ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 350), True)
        self._add_dialog(cast, RESTART_INSTRUCTIONS, FONT, FONT_SMALL,
                         ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 400), True)

        self._add_background(cast, BACKGROUND_GAME_OVER)
        self._add_dog_sad(cast,CENTER_X - DOG_WIDTH / 1.5, CENTER_Y - DOG_HEIGHT)


        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEXT_LEVEL, RESTART))
        script.add_action(INPUT, ChangeSceneAction(
            self.KEYBOARD_SERVICE, NEW_GAME, MENU))
        script.clear_actions(UPDATE)

        draw = [
            self.DRAW_BACKGROUND_ACTION,
            self.DRAW_DIALOG_ACTION,
            self.DRAW_DOG_SAD_ACTION
        ]

        self._add_output_script(script, draw)

        script.add_action(OUTPUT, PlaySoundAction(
            self.AUDIO_SERVICE, WELCOME_SOUND))

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _add_background(self, cast, image_path):
        cast.clear_actors(BACKGROUND_GROUP)
        x = 0
        y = 0
        position = Point(x, y)
        size = Point(SCREEN_WIDTH, SCREEN_HEIGHT)
        velocity = Point(0, 3)
        body = Body(position, size, velocity)
        animation = Animation(image_path, BG_RATE)
        background = Background(body, animation)
        cast.add_actor(BACKGROUND_GROUP, background)

    def _add_bones(self, cast):
        cast.clear_actors(BONE_GROUP)

        for i in range(BONE_QUANTITY):
            x = 600
            y = Y_DISTANCE * (i+1)
            position = Point(y, x)

            size = Point(BONE_WIDTH, BONE_HEIGHT)

            vel_x = random.randrange(-3, 9)
            vel_y = int((i+600)*0.01)

            velocity = Point(vel_y, vel_x)
            type_of_bone = random.randrange(0, 4)
            body = Body(position, size, velocity)
            bone = Bone(body, type_of_bone, True)

            cast.add_actor(BONE_GROUP, bone)

    def _add_dialog(self, cast, message, file, size, alignment, p_position, multiple=False):
        if multiple == False:
            cast.clear_actors(DIALOG_GROUP)
        label = Label(Text(message, file, size, alignment), p_position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_dog(self, cast):
        cast.clear_actors(DOG_GROUP)
        x = SCREEN_WIDTH - DOG_WIDTH * 1.5
        y = SCREEN_HEIGHT - DOG_HEIGHT * 1.3
        position = Point(x, y)
        size = Point(DOG_WIDTH, DOG_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(DOG_IMAGES, DOG_RATE)
        dog = Dog(body, animation)
        cast.add_actor(DOG_GROUP, dog)


    def _add_dog_sad(self, cast, dog_x, dog_y):
        cast.clear_actors(DOG_SAD_GROUP)
        position = Point(dog_x, dog_y)
        size = Point(DOG_WIDTH, DOG_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(DOG_SAD_IMAGES, DOG_SAD_RATE)
        dog = DogSad(body, animation)
        cast.add_actor(DOG_SAD_GROUP, dog)


    def _add_owner(self, cast):
        cast.clear_actors(OWNER_GROUP)
        x = -15
        y = (SCREEN_HEIGHT / 2)
        position = Point(x, y)
        size = Point(OWNER_WIDTH, OWNER_HEIGHT)
        velocity = Point(0, 3)
        body = Body(position, size, velocity)
        animation = Animation(OWNER_IMAGES, OWNER_RATE)
        owner = Owner(body, animation)
        cast.add_actor(OWNER_GROUP, owner)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)

    def _add_output_script(self, script, draw):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)

        for i in draw:
            script.add_action(OUTPUT, i)

        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)

    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)

    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BONES_ACTION)
        script.add_action(UPDATE, self.MOVE_DOG_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_DOG_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BONES_ACTION)
        script.add_action(UPDATE, self.MOVE_DOG_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
