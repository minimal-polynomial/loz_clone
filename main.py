import pygame

import sys

#from sprites import *

from modules.block import Block
from modules.button import Button
from modules.config import *
from modules.door import Door
from modules.enemy import Enemy
from modules.ground import Ground
#from modules.level import Level                                 # <- latest module; still in developemnt
from modules.player import Player
from modules.rangeattack import RangeAttack
from modules.spritesheet import Spritesheet
from modules.swordattack import SwordAttack

# TODOS:
# first problem: file paths are absolute. change code to relative file imports

# make abstact base classes for character and enemies and derive them from that

# make spritesheet.animatedspritesheet class that knows sprites as animation-up-2 to improve code readability

# create event that triggser when all enemies have been killed

# create protal sprite that allows player to exit next map

# create class for map that holds all tiles and can load files with the map configuration

# organize maps into differnt files

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        #self.playing = False
        # the ARCADECLASSIC font i only free for personal use! keep this in mind!
        self.font = pygame.font.Font('ARCADECLASSIC.TTF', 32)

        #self.script_dir = os.path.dirname(os.path.abspath(__file__))

        #character_spritesheet = pygame.image.load(os.path.join(self.script_dir, "img", "character.png"))
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')

        self.intro_background = pygame.image.load('img/introbackground.png')
        self.go_background = pygame.image.load('img/gameover.png')

        self.map_1 = map_1
        self.map_2 = map_2

    def create_tilemap(self, tilemap):
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
        

    def new_game(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()

        self.create_tilemap(map_1)

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:        # shouldn't this go to the player sprite class?
                if event.key == pygame.K_j:     # move this logic to a function anyways
                    if self.player.facing == 'up':
                        SwordAttack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        SwordAttack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        SwordAttack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        SwordAttack(self, self.player.rect.x + TILESIZE, self.player.rect.y)
            
            if event.type == pygame.KEYDOWN:        # display controls somewhere in menu
                if event.key == pygame.K_i:
                    if self.player.facing == 'up':
                        RangeAttack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        RangeAttack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        RangeAttack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        RangeAttack(self, self.player.rect.x + TILESIZE, self.player.rect.y)


    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main_loop(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))
        restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new_game()
                self.main_loop()


            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


    def show_intro_screen(self):
        intro = True

        title = self.font.render('Fabians Game', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        intro = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()



game = Game()
game.show_intro_screen()
game.new_game()
while game.running:
    game.main_loop()
    game.game_over()

pygame.quit()
sys.exit()