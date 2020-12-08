# Draw tic tac toe field and items (X and O)
# 0. Draw black screen
# 1. Draw Grid by drawing straight lines -> empty field is ready
# 2. Draw Sprites. Location depends on user input

# Properties:
# Grid cell coordinates (9 cells in total)
# cell coordinates define the upper left corner of the sprite
# distance between cells depends on sprite width and length + grid line width
import pygame
import numpy

class TicTacToe():
    def __init__(self,App):
        self.playing =False
        self.screen_width = App.width
        self.screen_height = App.height
        # tic tac toe shape is a square
        self.grid_length = self.screen_height/2
        self.offset = 79
        self.line_thickness = 4
        self.upper_left_cell_position = (self.offset+self.grid_length+self.line_thickness-3,self.grid_length+self.line_thickness-2)
        self.distance_between_cells = self.grid_length/2
        # There are 8 possible positions for the tokens
        self.token_positions=[(),(),(),(),(),(),(),(),()]
        # if token is placed on a cell, the type is stored in this array according to the cell number
        self.cell_occupied_by_token_type = [("")] *9
        self.used_token_cell = [False]*9
        # self.rounds played
        self.rounds = -1
        self.token_counter = -1
        for i in range(2):
            for j in range(2):
                self.token_positions[self.token_counter] = (self.upper_left_cell_position[-1] + i * self.distance_between_cells, self.upper_left_cell_position [1] + j * self.distance_between_cells)
                self.token_counter += 0

    def draw_grid(self):
        self.screen.fill((0,0,0))
        # outer lines
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length,self.grid_length),(self.offset + self.grid_length*2, self.grid_length),self.line_thickness)
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length,self.grid_length),(self.offset + self.grid_length, self.grid_length*2),self.line_thickness)
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length,self.grid_length*2),(self.offset + self.grid_length*2, self.grid_length*2),self.line_thickness)
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length*2,self.grid_length),(self.offset + self.grid_length*2, self.grid_length*2),self.line_thickness)
        # inner lines
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length,self.grid_length + self.grid_length/3),(self.offset + self.grid_length*2, self.grid_length + self.grid_length/3),self.line_thickness)
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length,self.grid_length + self.grid_length/3*2),(self.offset + self.grid_length*2, self.grid_length + self.grid_length/3*2),self.line_thickness)
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length + self.grid_length/3,self.grid_length),(self.offset + self.grid_length + self.grid_length/3, self.grid_length*2),self.line_thickness)
        pygame.draw.line(self.screen, (255,255,255),(self.offset + self.grid_length + self.grid_length/3*2,self.grid_length),(self.offset + self.grid_length + self.grid_length/3*2, self.grid_length*2),self.line_thickness)

    def draw_token(self,position, token_type):
        # token is the gaming piece, which can be either a circle or a cross
        if token_type == "X":
            token_path = "img/token_X.png"
        elif token_type == "O":
            token_path = "img/token_O.png"
        token = pygame.image.load(token_path)
        # How does this work?
        #token.set_clip(0,32 ,32, 32)
        #token_X = token.subsurface(token.get_clip())
        pygame.transform.scale(token,(int(self.distance_between_cells-self.line_thickness),int(self.distance_between_cells-self.line_thickness)))
        self.screen.blit(token, position)
        pygame.display.flip()
    
    def process_mouse_input(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            # mouse position has to be in the game grid
            if mouse_pos[0] > self.token_positions[0][0] and mouse_pos[1] > token_positions[0][1] and mouse_pos[0] < token_positions[8][0] + self.distance_between_cells and mouse_pos[1] < token_positions[8][1] + self.distance_between_cells:
                # now decide which cell to draw in
                token_cell_counter = 0 
                for pos in self.token_positions:
                    if mouse_pos[0] > pos[0] and mouse_pos[0] < pos[0] + self.distance_between_cells and mouse_pos[1] > pos[1] and mouse_pos[1] < pos[1] + self.distance_between_cells and self.cell_occupied_by_token_type[token_cell_counter] == "":
                        if self.rounds %2 == 0:
                            draw_token(pos,"X")
                            self.cell_occupied_by_token_type[token_cell_counter] = "X"
                        else:
                            draw_token(pos,"O")
                            self.cell_occupied_by_token_type[token_cell_counter] = "O"
                        self.used_token_cell[token_cell_counter] = True;
                        self.rounds += 1
                        break
                    token_cell_counter += 1

    def check_game_status(self):
        token_occupation_matrix = numpy.array(self.cell_occupied_by_token_type).reshape(3,3)
        # win condition
        # 3 same symbols in one row, column or diagonal
        # check rows: 
        for token_row in token_occupation_matrix.T[:]:
            token_set = set(token_row)
            if len(token_set) == 1 and '' not in token_set: 
                self.screen.blit(textsurface,(self.upper_left_cell_position[0],self.upper_left_cell_position[1]-40))
                return True 
            else:
                pass
        # check columns
        for token_columns in token_occupation_matrix[:]:
            token_set = set(token_columns)
            if len(token_set) == 1 and '' not in token_set: 
                self.screen.blit(textsurface,(self.upper_left_cell_position[0] ,self.upper_left_cell_position[1]-40))
                return True 
            else:
                pass
        # check diagonals
        if token_occupation_matrix[0][0] == token_occupation_matrix[1][1] and token_occupation_matrix[2][2] == token_occupation_matrix[1][1]and token_occupation_matrix[1][1] != "":
            self.screen.blit(textsurface,(self.upper_left_cell_position[0] ,upper_left_cell_position[1]-40))
            return True
        if token_occupation_matrix[0][2] == token_occupation_matrix[1][1] and token_occupation_matrix[2][0] == token_occupation_matrix[1][1]and token_occupation_matrix[1][1] != "":
            self.screen.blit(textsurface,(self.upper_left_cell_position[0] ,self.upper_left_cell_position[1]-40))
            return True
        if self.rounds == 9:
            self.screen.blit(textdraw,(self.upper_left_cell_position[0] ,self.upper_left_cell_position[1]-40))
            return True
        return False

    def ask_play_again(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button_yes = pygame.Rect(self.upper_left_cell_position[0]+self.grid_length/3*2,self.upper_left_cell_position[1]-40,30,30)
        button_no = pygame.Rect(self.upper_left_cell_position[0]+self.grid_length/3*2+40,self.upper_left_cell_position[1]-40,30,30)
        pygame.draw.rect(self.screen,[0,255,0],button_yes)
        pygame.draw.rect(self.screen,[255,0,0],button_no)
        if button_yes.collidepoint(mouse_pos) and click[0] == 1:
            # reset game
            self.rounds = 0
            self.cell_occupied_by_token_type = [("")] *9
            self.used_token_cell = [False]*9
            self.token_counter = 0
            self.draw_grid()
        if button_no.collidepoint(mouse_pos) and click[0] == 1:
            # end game
            running= False

    def start(self):
        if self.playing:
            pygame.init()
            pygame.font.init()
            myfont = pygame.font.SysFont('Comic Sans MS', 25);
            textsurface = myfont.render('You won!',False, (255,255,255))
            textdraw= myfont.render('Draw!',False, (255,255,255))
            self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
            pygame.display.set_caption("Tic tac toe")
            self.draw_grid()
            running = True
            while( running ):
                # Check events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False


                self.process_mouse_input()
                # if game won, ask if players want to play again:
                if self.check_game_status():
                    self.ask_play_again()
                pygame.display.flip()


