import pygame

from config import *

class RangeAttack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE

        self.direction = self.game.player.facing
        self.x_change = 0
        self.y_change = 0

        # dummy image just in case
        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)

        if self.direction == 'right':
            self.image = self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height)
        if self.direction == 'left':
            self.image =  self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height)
        if self.direction == 'up':
            self.image = self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height)
        if self.direction == 'down':
            self.image =  self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        #self.animate()      # no animation for range attacks atm
        self.movement()
        self.collide()

        self.rect.x += self.x_change                # movement should go to a seperate function
        #self.collide_blocks('x')
        self.rect.y += self.y_change
        #self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0


    def movement(self):
        if self.direction == 'right':
            self.x_change += PROJECTILE_SPEED
        if self.direction == 'left':
            self.x_change -= PROJECTILE_SPEED
        if self.direction == 'up':
            self.y_change -= PROJECTILE_SPEED
        if self.direction == 'down':
            self.y_change += PROJECTILE_SPEED


    def collide(self):
        hits_enemies = pygame.sprite.spritecollide(self, self.game.enemies, True)
        hits_blocks = pygame.sprite.spritecollide(self, self.game.blocks, False)          # destroy projectile upon hitting a block
        if hits_enemies or hits_blocks:
            self.kill()