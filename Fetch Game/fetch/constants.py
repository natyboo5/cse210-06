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
FONT_FILE = "fetch/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "fetch/assets/sounds/boing.wav"
WELCOME_SOUND = "fetch/assets/sounds/start.wav"
OVER_SOUND = "fetch/assets/sounds/over.wav"

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

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

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

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

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
DOG_VELOCITY = 7

# OWNER
OWNER_GROUP = "owners"
OWNER_IMAGES = [f"fetch/assets/images/{n:03}.png" for n in range(108, 111)]
OWNER_WIDTH = 20
OWNER_HEIGHT = 20
OWNER_RATE = 25

# BONE
BONE_GROUP = "bones"
BONE_QUANTITY = 1000
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

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"