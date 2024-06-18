TILESIZE = 32
FPS = 60

WIN_WIDTH = 20 * TILESIZE
WIN_HEIGHT = 15 * TILESIZE

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3
ENEMY_SPEED = 2
PROJECTILE_SPEED = 5

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B...E..............B',
    'B..................B',
    'B...BBB............B',
    'B..................B',
    'B..................B',
    'B..................B',
    'B.........P........B',
    'B..................B',
    'B..................B',
    'B........BBB.......B',
    'B..........B...E...B',
    'B..........B.......B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]