import pygame, random, sys, os
from modules.field import Field
from modules.constant import *

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#red, SIZE, NUM, black, OUTLINE, pic_1, pic_2, pic_3, pic_4, pic_5, pic_6, pic_7, pic_8, pic_9


# загрузка изображений.

asset_1 = resource_path('tiles/1.png')
one_asset = pygame.image.load(asset_1)
asset_2 = resource_path('tiles/2.png')
two_asset = pygame.image.load(asset_2)
asset_3 = resource_path('tiles/3.png')
three_asset = pygame.image.load(asset_3)
asset_4 = resource_path('tiles/4.png')
four_asset = pygame.image.load(asset_4)
asset_5 = resource_path('tiles/5.png')
five_asset = pygame.image.load(asset_5)
asset_6 = resource_path('tiles/6.png')
six_asset = pygame.image.load(asset_6)
asset_7 = resource_path('tiles/7.png')
seven_asset = pygame.image.load(asset_7)
asset_8 = resource_path('tiles/8.png')
eight_asset = pygame.image.load(asset_8)
asset_9 = resource_path('tiles/9.png')
nine_asset = pygame.image.load(asset_9)

asset_flag = resource_path('tiles/flag.jpg')
flag_asset = pygame.image.load(asset_flag)
asset_losing = resource_path('tiles/losing.jpg')
losing_asset = pygame.image.load(asset_losing)
asset_titry = resource_path('tiles/titry.jpg')
titry_asset = pygame.image.load(asset_titry)
asset_vanya_unflag = resource_path('tiles/vanya_unflag.jpg')
vanya_unflag_asset = pygame.image.load(asset_vanya_unflag)

#constants:
WIDTH = 640
HEIGHT = 640

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def get_row_col_from_mouse(pos):
    x, y = pos
    row = x // SIZE
    col = y // SIZE
    return row, col
#ЕБАТЬ ...
#rarely working
def spread(row, col, hoodfield, bombfield):
  
    def up(hoodfield, row, col):
            i, j = row, col
            while i < NUM and i >= 0 and j < NUM and j >= 0 and bombfield[i][j] == 0:
                if hoodfield[i][j] == 0: pygame.draw.rect(WIN, BLUE, (i * SIZE + OUTLINE, j * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))
                else: show_number(hoodfield, i, j, bombfield)
                j -= 1
        
           
    def right(hoodfield, row, col):
            i, j = row, col
            while  i < NUM and i >= 0 and j < NUM and j >= 0 and bombfield[i][j] == 0:
                if hoodfield[i][j] == 0: pygame.draw.rect(WIN, BLUE, (i * SIZE + OUTLINE, j * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))
                else: show_number(hoodfield, i, j, bombfield)
                i += 1
              
       
    
    def left(hoodfield, row, col):
            i, j = row, col
            while i < NUM and i >= 0 and j < NUM and j >= 0 and bombfield[i][j] == 0:
                if hoodfield[i][j] == 0:pygame.draw.rect(WIN, BLUE, (i * SIZE + OUTLINE, j * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))
                else: show_number(hoodfield, i, j, bombfield) 
                i -= 1
               
      
    def down(hoodfield, row, col):
            i, j = row, col
            while i < NUM and i >= 0 and j < NUM and j >= 0 and bombfield[i][j] == 0:
                if hoodfield[i][j] == 0: pygame.draw.rect(WIN, BLUE, (i * SIZE + OUTLINE, j * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))
                else: show_number(hoodfield, i, j, bombfield)
                j += 1
    def fill_krest(hoodfield, row, col):
        up(hoodfield, row, col)
        right(hoodfield, row, col)
        left(hoodfield, row, col)
        down(hoodfield, row, col)
    fill_krest(hoodfield, row, col)
             
    """
    Полное раскрытие синих полей и цифр.
    i = 1 # 1+2*i - диаметр квадрата
    j = 1 # аналогично
    while i<NUM and j<NUM:
        for a in range(1+2*i):
            for b in range(1+2*j):
                if a - i < NUM and b - j<NUM and bombfield[a - i][b - j]!=1: 
                    up(hoodfield, a - i, b - j)
                    down(hoodfield, a - i, b - j)
                    right(hoodfield, a - i, b - j)
                    left(hoodfield, a - i, b - j)
        i+=1
        j+=1
    
    # -= крест
   
   

        
"""
def show_number(hooder, row, col, bomber): # показывает значения hooder на экране
    # - pic_1.get_width() // 2,  - pic_2.get_height() // 2
    if hooder[row][col] == 0:
        pygame.draw.rect(WIN, BLUE, (row * SIZE + OUTLINE, col * SIZE + OUTLINE, SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
        spread(row, col, hooder, bomber)
    if hooder[row][col] == 1:
        WIN.blit(pic_1, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 2:
        WIN.blit(pic_2, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 3:
        WIN.blit(pic_3, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 4:
        WIN.blit(pic_4, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 5:
        WIN.blit(pic_5, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 6:
        WIN.blit(pic_6, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 7:
        WIN.blit(pic_7, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 8:
        WIN.blit(pic_8, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
    if hooder[row][col] == 9:
        WIN.blit(pic_9, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
def print_matrix(m):
    for i in range(len(m)):
        print(m[i], '\n')

    
def end():
    for row in range(NUM):
        for col in range(NUM):
            pygame.draw.rect(WIN, yellow, (row * SIZE, col * SIZE, SIZE, SIZE))
    for i in range(NUM):
        for j in range(NUM):
            if i == j or i == NUM - 1 - j: pygame.draw.rect(WIN, black, (i * SIZE, j * SIZE, SIZE, SIZE))
                

def main():
    run = True
    clock = pygame.time.Clock()
    field = Field(WIN)
    board = field.bombs
    hooder = field.hoods
    print_matrix(field.flags)
    Field.draw_squares(WIN)
    #pygame.draw.rect(WIN, yellow, (1 * SIZE + OUTLINE, 0 * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))
    
    #print_matrix(hooder)
    """
    for i in range(NUM):
        for j in range(NUM):
            if board[i][j] == 1:
                pygame.draw.rect(WIN, red, (i * SIZE + OUTLINE, j * SIZE + OUTLINE, SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
    """
    run_check = 1 # костыль для задержки времени
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    if field.flags[row][col] == 1:
                        WIN.blit(not_van, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
                    else: WIN.blit(flag, (row * SIZE + OUTLINE, col * SIZE + OUTLINE))
                    Field.flags_update(field, row, col) # костыль (row, col)
                   
                    if field.flags == field.bombs: 
                        WIN.blit(big_van, (0,0))
                    
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    #Field.flags_update(field, col, row) # костыль (row, col)
                    
                    if board[row][col] == 1:
                        pygame.draw.rect(WIN, red, (row * SIZE + OUTLINE, col * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))
                        WIN.blit(lose, (0,0))
                        run_check = 0
                        run = False
                    show_number(hooder, row, col, board)
        pygame.display.update()
        if not run_check:
            pygame.time.wait(3000)
    pygame.quit()
main()
