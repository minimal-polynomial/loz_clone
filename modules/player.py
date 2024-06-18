import pygame
import math

from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(3, 2)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        self.up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        self.left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

    def update(self):           # at some point rearrange this into smaller functions
        self.movement()
        self.animate()
        self.collide_enemy()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.collide_blocks('x')
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

        self.collide_doors()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        elif keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        elif keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        elif keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.game_over()

    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if direction == 'x':
            if hits:
                if self.x_change > 0:       # we're moving right
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED           # keep camera focussed
                if self.x_change < 0:        #we're moving left
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED    


        if direction == 'y':
            if hits:
                if self.y_change > 0:       # we're moving down
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED    
                if self.y_change < 0:       # we're moving up
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED 

    def collide_doors(self):
        hits = pygame.sprite.spritecollide(self, self.game.doors, False)
        if hits:
            print('Collide with door')
            print(hits[0].destination)
            for sprite in self.game.all_sprites:
                sprite.kill()     
            if hits[0].destination == 'a0':
                self.game.create_tilemap(self.game.map_1)
            if hits[0].destination == 'a1':
                self.game.create_tilemap(self.game.map_2)

    def animate(self):
        
        if self.facing == 'down':
            if self.y_change == 0:          # character stands still
                self.image = self.game.character_spritesheet.get_sprite(3, 2)
            else:
                self.image = self.down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'up':
            if self.y_change == 0:          # character stands still
                self.image = self.game.character_spritesheet.get_sprite(3, 34)
            else:
                self.image = self.up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'right':
            if self.x_change == 0:          # character stands still
                self.image = self.game.character_spritesheet.get_sprite(3, 66)
            else:
                self.image = self.right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == 'left':
            if self.x_change == 0:          # character stands still
                self.image = self.game.character_spritesheet.get_sprite(3, 98)
            else:
                self.image = self.left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1