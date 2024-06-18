import pygame

from config import *
from ground import Ground
from block import Block
from enemy import Enemy
from player import Player
from door import Door

class Level:
    def __init__(self, map):
        self.player = None

    def create_tilemap(self, tilemap) -> Player:
        for j, row in enumerate(tilemap):
            for i, tile in enumerate(row):
                Ground(self, i, j)
                if tile == 'B':
                    Block(self, i, j)
                if tile == 'E':
                    Enemy(self, i, j)
                if tile == 'P':
                    self.player = Player(self, i, j)
                if tile == 'D':
                    Door(self, i, j)

    def kill(self):
        pass            # kill all sprites; how do i access them?
    def get_player(self) -> Player:
        return self.player