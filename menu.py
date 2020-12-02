import pygame

class Menu():
    def __init__(self, App):
        self.App = App
        self.mid_w, self.mid_h = self.App.width/2, self.App.height/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
    

    def draw_text(self, text,size,x ,y):
        font = pygame.font.Font(self.App.font_name,size)
        text_surface = font.render(text, True, self.App.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center =(x,y)
        self.App.display.blit(text_surface,text_rect)

    def draw_cursor(self):
        self.draw_text('*',15,self.cursor_rect.x,self.cursor_rect.y)

    def blit_screen(self):
        self.App.display_surf.blit(self.App.display,(0,0))
        pygame.display.update()
        self.App.reset_keys()

class MainMenu(Menu):
    def __init__(self,App):
        Menu.__init__(self,App)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h+30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h+50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h+30
        self.cursor_rect.midtop = (self.startx + self.offset,self.starty)

    def display_menu(self):
        self.run_display = True
        while(self.run_display):
            self.App.check_events()
            self.App.display.fill(self.App.BLACK)
            self.draw_text('Main Menu', 20, self.App.width/2,self.App.height/2)
            self.draw_text("Start Game", 20, self.startx, self.starty)
            self.draw_text("Options", 20, self.optionsx,self.optionsy)
            self.draw_text("Credits",20,self.creditsx,self.creditsy)
            self.draw_cursor()

    
