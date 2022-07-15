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
BACKGROUND_LEVEL1 = [f"fetch/assets/images/{n:03}.png" for n in range(140, 144)]
BACKGROUND_LEVEL2 = [f"fetch/assets/images/{n:03}.png" for n in range(150, 151)]
BACKGROUND_LEVEL3 = [f"fetch/assets/images/{n:03}.png" for n in range(160, 161)]
BACKGROUND_FIRST_MENU = [f"fetch/assets/images/{n:03}.png" for n in range(0, 1)]
BACKGROUND_INSTRUCTIONS = [f"fetch/assets/images/{n:03}.png" for n in range(135, 136)]
BACKGROUND_GAME_OVER = [f"fetch/assets/images/{n:03}.png" for n in range(0, 1)]
BACKGROUND_GAME_OVER_WIN = [f"fetch/assets/images/{n:03}.png" for n in range(125, 126)]
BACKGROUND = [f"fetch/assets/images/{n:03}.png" for n in range(0, 1)]
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

DOG_SAD_GROUP = "dogs_sad"
DOG_SAD_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(190, 193)]
DOG_SAD_RATE = 30

# OWNER
OWNER_GROUP = "owners"
OWNER_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(108, 111)]
OWNER_WIDTH = 20
OWNER_HEIGHT = 20
OWNER_RATE = 25

# BONE
BONE_GROUP = "bones"
BONE_QUANTITY = 2000
Y_DISTANCE = -200
BONE_IMAGES = "fetch/assets/images/010.png"
BONE_MEAT_IMAGES = "fetch/assets/images/020.png"
BONE_WIDTH = 50
BONE_HEIGHT = 51
BONE_POINTS = 50
BONE_MEAT_POINTS = 200

# DYNAMITE
DYNAMITE_IMAGE = "fetch/assets/images/104.png"
DYNAMITE_POINTS = -50

# HEART
HEART_IMAGE = "fetch/assets/images/040.png"
HEART_POINTS = 100

HEART_WIN_GROUP = "hearts"
HEART_WIN_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(60, 65)]
HEART_WIN_WIDTH = 100
HEART_WIN_HEIGHT = 100
HEART_WIN_RATE = 25

# KEYBOARD
KEYBOARD_GROUP = "keyboars"
KEYBOARD_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(50, 54)]
KEYBOARD_WIDTH = 200
KEYBOARD_HEIGHT = 200
KEYBOARD_RATE = 25

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
WAS_GOOD_GAME_WIN = "CONGRATULATIONS"

# INSTRUCTIONS
HEART_INSTRUCTIONS = "1 life / 100 points / MAX 10"
BONE_INSTRUCTIONS = "50 points"
BONE_MEAT_INSTRUCTIONS = "200 points"
DYNAMITE_INSTRUCTIONS = "-1 life / -50 points"
FIRST_MENU_INSTRUCTIONS = "M - Menu"
RESTART_INSTRUCTIONS = "R - Restart"
SHOW_INSTRUCTIONS = "H - Help"
WARNING_1 = "Every 100 objects"
WARNING_2 = "SPEED will increase"
MOVE_DOG_1 = "To move your DOG"
WIN_DOG_1 = "To WIN"
WIN_DOG_2 = "Eat 500 objects"