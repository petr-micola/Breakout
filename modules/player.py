import pygame as pg


class Player:
    def __init__(self, screen, color, w, h, x, y):
        self.rect = None
        self.screen = screen
        self.color = color
        self.w = w
        self.h = h
        self.x = x / 2 - self.w / 2
        self.y = y - self.h * 2
        self.vel = 10
        self.speed = 0

    def check_collision(self, win):
        if win.colliderect(self.rect):
            return True

    def move(self, key, win_r, win_l):
        if (key[pg.K_d] or key[pg.K_RIGHT]) and not self.check_collision(win_r):
            self.x += self.vel
            self.speed = 1
        elif (key[pg.K_a] or key[pg.K_LEFT]) and not self.check_collision(win_l):
            self.x -= self.vel
            self.speed = -1

    def update(self):
        self.rect = pg.Rect((self.x, self.y), (self.w, self.h))
        pg.draw.rect(self.screen, self.color, self.rect)
        self.vel = 10
