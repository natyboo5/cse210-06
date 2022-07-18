import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Fetch"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 900
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT = "fetch/assets/fonts/Montserrat-Bold.otf"
FONT_SMALL = 32
FONT_LARGE = 48
FONT_SIZE_TITLE = 60

# SOUND
BOUNCE_SOUND = "fetch/assets/sounds/collision.wav"
GAME_SOUND = "fetch/assets/sounds/game_sound.wav"
OVER_SOUND = "fetch/assets/sounds/over.wav"
WELCOME_SOUND = "fetch/assets/sounds/welcome_page.wav"
NEW_LEVEL_SOUND = "fetch/assets/sounds/start.wav"


# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
MENU = "m"
HELP = "h"
RESTART = "r"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4
FIRST_MENU = 5
GAME_OVER_WIN = 6

# LEVELS
LEVEL_FILE = "fetch/assets/data/level-{:03}.txt"
BASE_LEVELS = 25

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# BACKGROUND
BACKGROUND_GROUP = "background"
BACKGROUND_LEVEL1 = "fetch/assets/images/140.png"
BACKGROUND_LEVEL2 = "fetch/assets/images/150.png"
BACKGROUND_LEVEL3 = "fetch/assets/images/160.png"
BACKGROUND_FIRST_MENU = "fetch/assets/images/000.png"
BACKGROUND_INSTRUCTIONS = "fetch/assets/images/000.png"
BACKGROUND_GAME_OVER = "fetch/assets/images/000.png"
BACKGROUND_GAME_OVER_WIN = "fetch/assets/images/000.png"
BACKGROUND = "fetch/assets/images/000.png"
BG_RATE = 15

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 10

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"


# DOG
DOG_GROUP = "dogs"
DOG_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(100, 104)]
DOG_WIDTH = 200
DOG_HEIGHT = 200
DOG_RATE = 6
DOG_VELOCITY = 10
GAME_DOG_X = SCREEN_WIDTH - DOG_WIDTH * 1.5
GAME_DOG_Y = SCREEN_HEIGHT - DOG_HEIGHT * 1.3
DOG_WIN_GAME_X = CENTER_X + 50
DOG_WIN_GAME_Y = CENTER_Y

DOG_SAD_GROUP = "dogs_sad"
DOG_SAD_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(190, 193)]
DOG_SAD_RATE = 30

# OWNER
OWNER_GROUP = "owners"
OWNER_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(108, 111)]
OWNER_WIDTH = 20
OWNER_HEIGHT = 20
OWNER_RATE = 25
OWNER_GAME_X = -15
OWNER_GAME_Y = (SCREEN_HEIGHT / 2)
OWNER_WIN_GAME_X = CENTER_X - 330
OWNER_WIN_GAME_Y = CENTER_Y - 150

# BONE
BONE_GROUP = "bones"
BONE_QUANTITY = 2000
Y_DISTANCE = -200
BONE_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(10, 12)]
BONE_MEAT_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(20, 22)]
BONE_WIDTH = 50
BONE_HEIGHT = 51
BONE_POINTS = 50
BONE_MEAT_POINTS = 200

# BONE HELP
BONE_HELP_GROUP = "randomimage"
RATE_ITEMS_HELP = 20

# DYNAMITE
DYNAMITE_IMAGE = [f"fetch/assets/images/{n:03}.png" for n in range(30, 32)]
DYNAMITE_POINTS = -50

# HEART
HEART_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(40, 42)]
HEART_POINTS = 100

HEART_WIN_GROUP = "hearts"
HEART_WIN_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(60, 65)]
HEART_WIN_WIDTH = 100
HEART_WIN_HEIGHT = 100
HEART_WIN_RATE = 25

RATE_ITEMS = 5

# KEYBOARD
KEYBOARD_GROUP = "keyboars"
KEYBOARD_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(50, 54)]
KEYBOARD_WIDTH = 200
KEYBOARD_HEIGHT = 200
KEYBOARD_RATE = 25

# FETCH TITLE
FETCH_TITLE_GROUP = "fetchtitle"
FETCH_TITLE_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(70, 73)]
FETCH_TITLE_WIDTH = 200
FETCH_TITLE_HEIGHT = 200
FETCH_TITLE_RATE = 25

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
WAS_GOOD_GAME_WIN = "CONGRATULATIONS"

# INSTRUCTIONS
HEART_INSTRUCTIONS = "1 life / 100 points / MAX 10"
BONE_INSTRUCTIONS = "50 points"
BONE_MEAT_INSTRUCTIONS = "200 points"
DYNAMITE_INSTRUCTIONS = "-1 life / -50 points"
FIRST_MENU_INSTRUCTIONS = "Press M - Main Menu"
RESTART_INSTRUCTIONS = "Press R - Restart"
SHOW_INSTRUCTIONS = "Press H - Help"
WARNING_1 = "Every 100 objects"
WARNING_2 = "SPEED will increase"
MOVE_DOG_1 = "To move your DOG"
WIN_DOG_1 = "To WIN"
WIN_DOG_2 = "Fetch 500 objects"