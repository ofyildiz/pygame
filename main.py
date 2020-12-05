import animate
import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._clock = pygame.time.Clock()

        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.FPS = 60

        self.avatar = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.avatar = animate.Animation('img/characters.png', rows=4, cols=23, pos=0, num=4)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self._display_surf.fill(pygame.color.Color('black'))
        self.avatar.update(self._display_surf)

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
