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

screen_width = 640
screen_height = 480
# tic tac toe shape is a square
grid_length = screen_height/3
offset = 80
line_thickness = 5
upper_left_cell_position = (offset+grid_length+line_thickness-2,grid_length+line_thickness-2)
distance_between_cells = grid_length/3
# There are 9 possible positions for the tokens
token_positions=[(),(),(),(),(),(),(),(),()]
# if token is placed on a cell, the type is stored in this array according to the cell number
cell_occupied_by_token_type = [("")] *9
used_token_cell = [False]*9
# rounds played
rounds = 0
token_counter = 0
for i in range(3):
    for j in range(3):
        token_positions[token_counter] = (upper_left_cell_position[0] + i * distance_between_cells, upper_left_cell_position [1] + j * distance_between_cells)
        token_counter += 1

def draw_grid():
    screen.fill((0,0,0))
    # outer lines
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length),(offset + grid_length*2,grid_length),line_thickness)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length),(offset + grid_length,grid_length*2),line_thickness)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length*2),(offset + grid_length*2,grid_length*2),line_thickness)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length*2,grid_length),(offset + grid_length*2,grid_length*2),line_thickness)
    # inner lines
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length + grid_length/3),(offset + grid_length*2,grid_length + grid_length/3),line_thickness)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length + grid_length/3*2),(offset + grid_length*2,grid_length + grid_length/3*2),line_thickness)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length + grid_length/3,grid_length),(offset + grid_length + grid_length/3,grid_length*2),line_thickness)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length + grid_length/3*2,grid_length),(offset + grid_length + grid_length/3*2,grid_length*2),line_thickness)

def draw_token(position, token_type):
    # token is the gaming piece, which can be either a circle or a cross
    if token_type == "X":
        token_path = "img/token_X.png"
    elif token_type == "O":
        token_path = "img/token_O.png"
    token = pygame.image.load(token_path)
    # How does this work?
    #token.set_clip(0,32 ,32, 32)
    #token_X = token.subsurface(token.get_clip())
    pygame.transform.scale(token,(int(distance_between_cells-line_thickness),int(distance_between_cells-line_thickness)))
    screen.blit(token, position)
    pygame.display.flip()
    
def process_mouse_input():
    global rounds
    # For some reason I don't need to declare the below as global
    global used_token_cell
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        # mouse position has to be in the game grid
        if mouse_pos[0] > token_positions[0][0] and mouse_pos[1] > token_positions[0][1] and mouse_pos[0] < token_positions[8][0] + distance_between_cells and mouse_pos[1] < token_positions[8][1] + distance_between_cells:
            # now decide which cell to draw in
            token_cell_counter = 0 
            for pos in token_positions:
                if mouse_pos[0] > pos[0] and mouse_pos[0] < pos[0] + distance_between_cells and mouse_pos[1] > pos[1] and mouse_pos[1] < pos[1] + distance_between_cells and cell_occupied_by_token_type[token_cell_counter] == "":
                    if rounds %2 == 0:
                        draw_token(pos,"X")
                        cell_occupied_by_token_type[token_cell_counter] = "X"
                    else:
                        draw_token(pos,"O")
                        cell_occupied_by_token_type[token_cell_counter] = "O"
                    used_token_cell[token_cell_counter] = True;
                    rounds += 1
                    break
                token_cell_counter += 1

def check_game_status():
    token_occupation_matrix = numpy.array(cell_occupied_by_token_type).reshape(3,3)
    # win condition
    # 3 same symbols in one row, column or diagonal
    # check rows: 
    for token_row in token_occupation_matrix.T[:]:
        token_set = set(token_row)
        if len(token_set) == 1 and '' not in token_set: 
            print("you won")
            return True 
        else:
            pass

    # check columns
    for token_columns in token_occupation_matrix[:]:
        token_set = set(token_columns)
        if len(token_set) == 1 and '' not in token_set: 
            print("you won")
            return True 
        else:
            pass
    return False


pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tic tac toe")
draw_grid()
running = True
while( running ):
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    check_game_status()
    process_mouse_input()
    pygame.display.flip()


