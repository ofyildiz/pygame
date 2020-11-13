# Draw tic tac toe field and items (X and O)
# 0. Draw black screen
# 1. Draw Grid by drawing straight lines -> empty field is ready
# 2. Draw Sprites. Location depends on user input

# Properties:
# Grid cell coordinates (9 cells in total)
# cell coordinates define the upper left corner of the sprite
# distance between cells depends on sprite width and length + grid line width

import pygame

screen_width = 640
screen_height = 480
# tic tac toe shape is a square
grid_length = screen_height/3
offset = 80
line_thickness = 5
upper_left_cell_position = (offset+grid_length+line_thickness,grid_length+line_thickness)
distance_between_cells = grid_length/3
token_positions=[(),(),(),(),(),(),(),(),()]
token_counter = 0
for i in range(3):
    for j in range(3):
        token_positions[token_counter] = (upper_left_cell_position[0] + i * distance_between_cells, upper_left_cell_position [1] + j * distance_between_cells)
        token_counter += token_counter

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
        token_path = ""
    elif token_type == "O":
        token_path = ""
    token = pygame.image.load(token_path)
    pygame.transform.scale(token,distance_between_cells-line_thickness)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tic tac toe")

running = True
while( running ):
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid()
    pygame.display.flip()


