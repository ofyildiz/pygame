import pygame

class Menu():
    def __init__(self, App):
        self.App = App
        self.mid_w, self.mid_h = self.App.width/2, self.App.height/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -70
    

    def draw_text(self, text,size,x ,y):
        font = pygame.font.Font(self.App.font_name,size)
        text_surface = font.render(text, True, self.App.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center =(x,y)
        self.App.display.blit(text_surface,text_rect)

    def draw_cursor(self):
        self.draw_text('*',30,self.cursor_rect.x,self.cursor_rect.y)

    def blit_screen(self):
        self.App._display_surf.blit(self.App.display,(0,0))
        pygame.display.update()
        self.App.reset_keys()

class MainMenu(Menu):
    def __init__(self,App):
        Menu.__init__(self,App)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h+30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h+60
        self.creditsx, self.creditsy = self.mid_w, self.mid_h+90
        self.cursor_rect.midtop = (self.startx + self.offset,self.starty+7)

    def display_menu(self):
        while(self.run_display):
            self.App.check_events()
            self.check_input()
            self.App.display.fill(self.App.BLACK)
            self.draw_text('Main Menu', 20, self.App.width/2,self.App.height/2-30)
            self.draw_text("Start Game", 20, self.startx, self.starty)
            self.draw_text("Options", 20, self.optionsx,self.optionsy)
            self.draw_text("Credits",20,self.creditsx,self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.App.DOWN_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy+7)
                self.state = "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy+7)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty+7)
                self.state = "Start"
        if self.App.UP_KEY:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy+7)
                self.state = "Credits"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty+7)
                self.state = "Start"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy+5)
                self.state = "Options"

    def check_input(self):
        self.move_cursor()
        if self.App.START_KEY:
            if self.state == "Start":
                self.run_display = False
                self.App.playing = True
            elif self.state == "Options":
                self.run_display = False
                self.App.tictactoe.playing = True
            elif self.state == "Credits":
                self.run_display = False
                self.App.curr_menu = CreditsMenu(self.App)

class CreditsMenu(Menu):
    def __init__(self, App):
        Menu.__init__(self, App)

    def display_menu(self):
        while self.run_display:
            self.App.check_events()
            self.App.display.fill(self.App.BLACK)
            self.draw_text('Credits', 20, self.App.width / 2, self.App.height/ 2 - 20)
            self.draw_text('Made by Ömario and Yöshi', 15, self.App.width/ 2, self.App.height/ 2 + 10)
            self.blit_screen() 