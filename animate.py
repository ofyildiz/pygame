import csv
import pygame
from pygame.locals import *

class Animation:
    def __init__(self, filepath, rows=1, cols=1, pos=0, num=1, x=0, y=0, vel=16, w=640, h=400):
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
        self.num = num
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
        self.posidx = [self.x//self.charwidth, self.y//self.charheight]

    def update(self, display, background):
        if pygame.key.get_pressed()[pygame.K_RIGHT] and background.array[self.posidx[1]][self.posidx[0]+1] != 'w':
            self.x += self.vel
            self.posidx[0] += 1
            pygame.time.wait(200)
        elif pygame.key.get_pressed()[pygame.K_LEFT] and background.array[self.posidx[1]][self.posidx[0]-1] != 'w':
            self.x -= self.vel
            self.posidx[0] -= 1
            pygame.time.wait(200)
        elif pygame.key.get_pressed()[pygame.K_UP] and background.array[self.posidx[1]-1][self.posidx[0]] != 'w':
            self.y -= self.vel
            self.posidx[1] -= 1
            pygame.time.wait(200)
        elif pygame.key.get_pressed()[pygame.K_DOWN] and background.array[self.posidx[1]+1][self.posidx[0]] != 'w':
            self.y += self.vel
            self.posidx[1] += 1
            pygame.time.wait(200)
        display.blit(self.sprites[self.imidx//(60//self.num)], (self.x, self.y))
        if self.imidx+1 == 60:
            self.imidx = 0
        else:
            self.imidx += 1

class Background:
    def __init__(self, filepath, w=16, h=16):
        self.w = w
        self.h = h
        with open(filepath) as csvfile:
            self.array = list(csv.reader(csvfile, delimiter=' '))

    def update(self, display):
        for rowKey, rowElem in enumerate(self.array):
            for colKey, colElem in enumerate(rowElem):
                if colElem == 'w':
                    pygame.draw.rect(display, pygame.color.Color('blue'), pygame.Rect(colKey*self.w, rowKey*self.h, self.w, self.h))
                elif colElem == 'g':
                    pygame.draw.rect(display, pygame.color.Color('green'), pygame.Rect(colKey*self.w, rowKey*self.h, self.w, self.h))
