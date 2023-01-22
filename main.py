import sys

import pygame as pg
from pygame.locals import *

from modules.player import Player
from modules.ball import Ball
from modules.block import Block

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Game:
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
        pg.display.set_caption('Pygame hra')
        # pg.display.set_icon()
        self.image = pg.image.load('image.jpg')

        self.player = Player(self.screen, RED, 80, 8, self.width, self.height)
        self.ball = Ball(self.screen, WHITE, 8, self.width, self.height)
        self.blocks = []
        self.block_x = 80
        for i in range(1, 28):
            self.block = Block(self.screen, GREEN, 40, 6, self.block_x, self.height)
            self.blocks.append(self.block)
            self.block_x += 60
            if i % 9 == 0:
                self.block_x = 80
                self.height += 200

    def run(self):
        while True:
            # self.screen.blit(self.image, (0, 0))
            self.screen.fill(BLACK)

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            key = pg.key.get_pressed()
            self.player.move(key)

            self.player.update()
            self.ball.update()
            for block in self.blocks:
                block.update()

            self.ball.check_collision(self.player, self.blocks, self.win_t, self.win_r, self.win_b, self.win_l)

            pg.display.flip()
            self.fpsClock.tick(self.fps)


if __name__ == '__main__':
    g = Game()
    g.run()
