import pygame

from config import *

class Spritesheet():
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width = TILESIZE, height = TILESIZE) -> pygame.Surface:      # make this method more conveinient by just having to call ()'up',1), ('up',2) etc
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite