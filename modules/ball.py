import pygame as pg


class Ball:
    # vytvoření míče za pomocí parametrů
    def __init__(self, screen, color, r, x, y):
        self.rect = None
        self.screen = screen
        self.color = color
        self.r = r
        self.x = x / 2 - self.r / 2
        self.y = y / 2 - self.r / 2
        self.vel_x = 0
        self.vel_y = 6

    # detekce kolize s hráčem, bloky a okrajem obrazovky
    def check_collision(self, player, blocks, win_t, win_r, win_b, win_l):
        if player.rect.colliderect(self.rect):
            if player.speed > 0:
                self.vel_x = 3
            elif player.speed:
                self.vel_x = -3
            self.vel_y *= -1

        for block in blocks:
            if block.rect.colliderect(self.rect):
                blocks.pop(blocks.index(block))
                self.vel_y *= -1

        if win_t.colliderect(self.rect):
            self.vel_y *= -1
        elif win_r.colliderect(self.rect) or win_l.colliderect(self.rect):
            self.vel_x *= -1
        elif win_b.colliderect(self.rect):
            return True

    # znovuvykreslení objektu
    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect = pg.Rect((self.x, self.y), (self.r, self.r))
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
