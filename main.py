import animate
import pygame
from pygame.locals import *
import menu
import TicTacToe

class App:
    def __init__(self):
        # Flag to indicate if the whole game/software is running
        self._running = True
        # Flag to indicate if the game (after you click "start  game") is playing
        self.playing = False
        self._clock = pygame.time.Clock()

        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.FPS = 60

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.font_name = pygame.font.get_default_font()
        #pygame.font.init()
        #self.font_name = pygame.font.SysFont("arial",20)
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.display = pygame.Surface((self.width,self.height))
        self.main_menu = menu.MainMenu(self)
        self.curr_menu = self.main_menu
        self.tictactoe = TicTacToe.TicTacToe(self)

    def check_events(self):
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              self.running= False
              self.curr_menu.run_display = False
          if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RETURN:
                  self.START_KEY = True
             if event.key == pygame.K_BACKSPACE:
                  self.BACK_KEY = True
             if event.key == pygame.K_DOWN:
                 self.DOWN_KEY = True
             if event.key == pygame.K_UP:
                  self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.avatar = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.avatar = animate.Animation('img/characters.png', rows=4, cols=23, pos=0, num=4)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        if self.playing:
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

        while(self._running):
            self.check_events()
            if self.BACK_KEY:
                self.playing = False
                self.main_menu.run_display = True
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self.curr_menu.display_menu()
            self.tictactoe.start()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
