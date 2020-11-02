import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._clock = pygame.time.Clock()

        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.FPS = 60

        self.charsheet = None
        self.char_baby = []
        self.x = self.width//2
        self.y = self.height//2
        self.vel = 5
        self.char_king = None
        self.char_squire = None
        self.char_snake = None
        self.charsize = self.charwidth, self.charheight = 32, 32
        self.imidx = 0
        self.imidy = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.charsheet = pygame.image.load("img/characters.png")
        self.charsheet2 = pygame.image.load("img/white.png")

        for idx in range(4):
            self.charsheet.set_clip(idx*self.charwidth, 0, self.charwidth, self.charheight)
            self.char_baby.append(self.charsheet.subsurface(self.charsheet.get_clip()))

        self.charsheet.set_clip(0, self.charheight, self.charwidth, self.charheight)
        self.char_king = self.charsheet.subsurface(self.charsheet.get_clip())

        self.charsheet.set_clip(0, 2*self.charheight, self.charwidth, self.charheight)
        self.char_squire = self.charsheet.subsurface(self.charsheet.get_clip())

        self.charsheet.set_clip(0, 3*self.charheight, self.charwidth, self.charheight)
        self.char_snake = self.charsheet.subsurface(self.charsheet.get_clip())

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x + self.vel <= self.width - self.charwidth:
            self.x += self.vel
        elif pygame.key.get_pressed()[pygame.K_LEFT] and self.x - self.vel >= 0:
            self.x -= self.vel
        elif pygame.key.get_pressed()[pygame.K_UP] and self.y - self.vel >=0:
            self.y -= self.vel
        elif pygame.key.get_pressed()[pygame.K_DOWN] and self.y + self.vel <= self.height - self.charheight:
            self.y += self.vel
        self._display_surf.fill(pygame.color.Color('black'))
        self._display_surf.blit(self.char_baby[self.imidy], (self.x, self.y))
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
        self._display_surf.blit(self.char_king, (50,150))
        self._display_surf.blit(self.char_squire, (50,250))
        self._display_surf.blit(self.char_snake, (50,350))
        self._display_surf.blit(self.charsheet2, (150,350))

    def on_render(self):
        pygame.display.flip()
        self._clock.tick(self.FPS)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
