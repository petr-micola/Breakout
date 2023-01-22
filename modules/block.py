import pygame as pg


class Block:
    def __init__(self, screen, color, w, h, x, y):
        self.rect = None
        self.screen = screen
        self.color = color
        self.w = w
        self.h = h
        self.x = x - self.w / 2
        self.y = y - y / 1.1 - self.h * 2
        # self.vel = 10
        # self.speed = 0

    def update(self):
        self.rect = pg.Rect((self.x, self.y), (self.w, self.h))
        pg.draw.rect(self.screen, self.color, self.rect)
