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

#   -1 = . = Empty
#   00 = P = Player
#   01 = E = Enemy 1
#   10 = B = Block 0 (Rock)
#   20 = D = Door 0

map_1_old = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B...E..............B',
    'B..................B',
    'B...BBB............B',
    'B..................B',
    'B..................B',
    'B..................D',
    'B.........P........D',
    'B..................B',
    'B..................B',
    'B........BBB.......B',
    'B..........B...E...B',
    'B..........B.......B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB'
]

map_1 = [
    [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11],
    [10,-1,-1,-1 ,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,10,10,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,20],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,00,-1,-1,-1,-1,-1,-1,-1,-1,-1,20],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,12,12,-1,-1,-1 ,1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12,-1,-1,-1,-1,-1,-1,11],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,11],
    [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11],
]

map_2_old = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B...E..............B',
    'B..................B',
    'B...BBBBBBBB.......B',
    'B..........B.......B',
    'B....E.....B.......B',
    'B..........B.......D',
    'B.....E....B.......D',
    'B..........B.......B',
    'B..E.......B.......B',
    'B........BBB.......B',
    'B..........B...E...B',
    'B......E...B.......B',
    'B..P...............B',
    'BBBBBBBBBBBBBBBBBBBB'
]

map_2 = [
    [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
    [10,-1,-1,-1 ,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,10,10,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [21,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [21,-1,-1,-1,-1,-1,-1,-1,-1,00,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,10,10,-1,-1,-1 ,1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10,-1,-1,-1,-1,-1,-1,10],
    [10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
    [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
]