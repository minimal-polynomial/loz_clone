import pygame
from config import *

class Door(pygame.sprite.Sprite):
    def __init__(self, game, x, y, direction, destination):

        self.game = game
        self.direction = direction
        self.destination = destination
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.doors
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        if direction == 'right':
            self.image = self.game.arrow_spritesheet.get_sprite(0, 0)
        if direction == 'up':
            self.image = self.game.arrow_spritesheet.get_sprite(32, 0)
        if direction == 'left':
            self.image = self.game.arrow_spritesheet.get_sprite(64, 0)
        if direction == 'down':
            self.image = self.game.arrow_spritesheet.get_sprite(96, 0)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y