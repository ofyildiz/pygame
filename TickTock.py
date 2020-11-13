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
def draw_grid():
    screen.fill((0,0,0))
    # outer lines
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length),(offset + grid_length*2,grid_length),5)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length),(offset + grid_length,grid_length*2),5)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length*2),(offset + grid_length*2,grid_length*2),5)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length*2,grid_length),(offset + grid_length*2,grid_length*2),5)
    # inner lines
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length + grid_length/3),(offset + grid_length*2,grid_length + grid_length/3),5)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length,grid_length + grid_length/3*2),(offset + grid_length*2,grid_length + grid_length/3*2),5)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length + grid_length/3,grid_length),(offset + grid_length + grid_length/3,grid_length*2),5)
    pygame.draw.line(screen, (255,255,255),(offset + grid_length + grid_length/3*2,grid_length),(offset + grid_length + grid_length/3*2,grid_length*2),5)

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


