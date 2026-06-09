from pathlib import Path
import pygame

WIDTH = 1200
HEIGHT = 800
FPS = 60

HEX_SIZE = 32
MAP_COLS = 17
MAP_ROWS = 12
UNIT_IMAGE_SIZE = 42

ASSET_ROOT = Path("assets")
UNIT_ASSET_ROOT = ASSET_ROOT / "units"

BG = (28, 26, 22)
PANEL = (38, 35, 30)
GRID = (95, 85, 65)
TEXT = (235, 225, 205)
MUTED = (170, 160, 140)
SELECT = (255, 230, 120)
BUTTON = (62, 58, 50)
BUTTON_HOVER = (82, 76, 64)

BLUE = (70, 130, 220)
RED = (190, 70, 60)
BROWN = (145, 95, 55)
HIDDEN = (65, 55, 50)

PLAIN = (92, 116, 62)
ROUGH = (88, 80, 62)
PREPARED = (125, 105, 58)
SUPPLY = (75, 110, 135)
DEPLOY = (65, 95, 125)
HEIGHTS = (115, 92, 63)
FROZEN = (112, 132, 140)
VILLAGE = (120, 85, 70)
BEACH = (185, 160, 105)
SEA = (55, 85, 120)
BLOCKADE = (40, 120, 155)
BOCAGE = (60, 95, 55)
BUNKER = (95, 95, 95)
DROPZONE = (90, 110, 80)
DESERT = (160, 130, 70)
AIRFIELD = (90, 90, 85)
OBJECTIVE = (120, 100, 40)
FOREST = (45, 90, 48)
CITY = (105, 95, 85)
BRIDGE = (125, 90, 55)
RIVER = (45, 95, 135)
ROAD = (125, 110, 80)

BACK_BUTTON_RECT = pygame.Rect(775, 744, 370, 34)
PRINCIPLE_DROPDOWN_RECT = pygame.Rect(230, 105, 740, 42)

DROPDOWN_OPTION_HEIGHT = 44
DROPDOWN_PANEL_PADDING = 6
DROPDOWN_MAX_VISIBLE_OPTIONS = 6

DIRECTIONS = [
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
]

TERRAIN_COLORS = {
    "plain": PLAIN,
    "rough": ROUGH,
    "prepared": PREPARED,
    "supply": SUPPLY,
    "heights": HEIGHTS,
    "frozen": FROZEN,
    "village": VILLAGE,
    "beach": BEACH,
    "sea": SEA,
    "blockade": BLOCKADE,
    "bocage": BOCAGE,
    "bunker": BUNKER,
    "dropzone": DROPZONE,
    "desert": DESERT,
    "airfield": AIRFIELD,
    "objective": OBJECTIVE,
    "forest": FOREST,
    "city": CITY,
    "bridge": BRIDGE,
    "river": RIVER,
    "road": ROAD,
}
