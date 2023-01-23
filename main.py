import sys

import pygame as pg
from pygame.locals import *

from modules.player import Player
from modules.ball import Ball
from modules.block import Block

# konstanty pro barvy
WHITE = '#edf6f9'
BLUE = '#83c5be'


class Game:
    # základní nastavení hry, vytvoření objektů
    def __init__(self):
        pg.init()

        self.fps = 60
        self.fpsClock = pg.time.Clock()

        self.width, self.height = 640, 520
        self.win_t = pg.Rect((0, -self.height), (self.width, self.height))
        self.win_r = pg.Rect((self.width, 0), (self.width, self.height))
        self.win_b = pg.Rect((0, self.height), (self.width, self.height))
        self.win_l = pg.Rect((-self.width, 0), (self.width, self.height))
        self.screen = pg.display.set_mode((self.width, self.height))
        self.image = pg.image.load('assets/image.jpg')
        self.icon = pg.image.load('assets/icon.png')

        pg.display.set_caption('Breakout')
        pg.display.set_icon(self.icon)

        self.player = Player(self.screen, WHITE, 80, 8, self.width, self.height)
        self.ball = Ball(self.screen, BLUE, 8, self.width, self.height)
        self.blocks = []
        self.block_x = 80
        for i in range(1, 37):
            self.block = Block(self.screen, WHITE, 40, 6, self.block_x, self.height)
            self.blocks.append(self.block)
            self.block_x += 60
            if i % 9 == 0:
                self.block_x = 80
                self.height += 200

    # rozjetí hry, pohyb, znovuvykreslování a kolize objektů, vyhodnocení konce hry
    def run(self):
        while True:
            self.screen.blit(self.image, (0, 0))

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            key = pg.key.get_pressed()
            self.player.move(key, self.win_r, self.win_l)

            self.player.update()
            self.ball.update()
            for block in self.blocks:
                block.update()

            if len(self.blocks) == 0:
                self.screen.blit(pg.image.load('assets/winner.jpg'), (0, 0))

            if self.ball.check_collision(self.player, self.blocks, self.win_t, self.win_r, self.win_b, self.win_l) or \
                    key[K_r]:
                pg.quit()
                new_g = Game()
                new_g.run()

            pg.display.flip()
            self.fpsClock.tick(self.fps)


if __name__ == '__main__':
    g = Game()
    g.run()
