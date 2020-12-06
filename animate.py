import pygame
from pygame.locals import *

class Animation:
    def __init__(self, filepath, rows=1, cols=1, pos=0, num=1, x=0, y=0, vel=5, w=640, h=400):
        """
        This class handles animation, meaning sprites or collection of sprites.
        The input:

        filepath - (string) path to sprite or spritesheet
        rows - (int) number of rows in spritesheet
        cols - (int) number of cols in spritesheet
        pos - (int) row identifier
        num - (int) number of sprites (as used in animation)
        x - (int) starting x position
        y - (int) starting y position
        vel - (int) velocity of object
        w - (int) maximum screen width
        h - (int) maximum screen height

        The output:
            sprites - (list) list of unique sprites
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel = vel

        self.sprites = []

        image = pygame.image.load(filepath)
        self.charwidth = image.get_width()//cols
        self.charheight = image.get_height()//rows

        for idx in range(num):
            image.set_clip(idx*self.charwidth, pos, self.charwidth, self.charheight)
            self.sprites.append(image.subsurface(image.get_clip()))

        self.imidx = 0
        self.imidy = 0

    def update(self, display):
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x + self.vel <= self.w - self.charwidth:
            self.x += self.vel
        elif pygame.key.get_pressed()[pygame.K_LEFT] and self.x - self.vel >= 0:
            self.x -= self.vel
        elif pygame.key.get_pressed()[pygame.K_UP] and self.y - self.vel >=0:
            self.y -= self.vel
        elif pygame.key.get_pressed()[pygame.K_DOWN] and self.y + self.vel <= self.h - self.charheight:
            self.y += self.vel
        display.blit(self.sprites[self.imidy], (self.x, self.y))
        if self.imidx+1 == 60:
            self.imidx = 0
            self.imidy = 0
        elif 0 <= self.imidx+1 < 15:
            self.imidx += 1
            self.imidy = 0
        elif 15 <= self.imidx+1 < 30:
            self.imidx += 1
            self.imidy = 1
        elif 30 <= self.imidx+1 < 45:
            self.imidx += 1
            self.imidy = 2
        elif 45 <= self.imidx+1 < 60:
            self.imidx += 1
            self.imidy = 3
