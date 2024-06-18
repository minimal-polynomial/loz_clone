import pygame
from config import *

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image = 'tree'):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        if image == 'rock':
            self.image = self.game.terrain_spritesheet.get_sprite(960, 448)
        elif image == 'tree':
            self.image = self.game.tree_spritesheet.get_sprite(0, 0)
        elif image == 'appletree':
            self.image = self.game.tree_spritesheet.get_sprite(32, 0)
        else:
            # raise error instead
            print('Block image unknown')

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y