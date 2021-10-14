import random, pygame
from modules.constant import *
class Field:

    def __init__(self, WIN): # создаем экземпляр Field, со свойствами bombs = минному полю, hoods = оценочному полю, flags
        self.WIN = WIN
        Field.bombs(self)
        Field.hoods(self)
        self.flags = Field.create_map(NUM)
        Field.fill_with_zeros(self.flags)

    #Все вспомогательные методы
    @staticmethod
    def create_map(NUM): # метод, создающий пустую матрицу NUM X NUM
        mapp = []
        for i in range(NUM):
            mapp.append([])
            for j in range(NUM):
                mapp[i].append([])
        return mapp
    @staticmethod
    def draw_squares(win): #win == windows, метод создает видимое поле
        win.fill(black)
        for row in range(NUM):
            for col in range(NUM):
                pygame.draw.rect(win, black, (row * SIZE, col * SIZE, SIZE, SIZE))
                pygame.draw.rect(win, GREY, (row * SIZE + OUTLINE , col * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))
    @staticmethod
    #проверка рандомности разрядов в матрице
    def rand_check(field):
        different = 0
        for i in range(NUM - 1):
            for j in range(NUM):
                if field[i][j] != field[i+1][j]:
                    different += 1
        return different
    @staticmethod
    def fill_borders_corners(cif,field): # заполняет углы и границы hoods
            
        cif[0][0] = field[0][1] + field[1][0] + field[1][1]
        cif[NUM - 1][0] = field[NUM - 1][1] + field[NUM - 2][0] + field[NUM - 2][1]
        cif[0][NUM - 1] = field[0][NUM-2] + field [1][NUM - 1] + field [1][NUM - 2]
        cif[NUM - 1][NUM - 1] = field[NUM - 1][NUM - 2] + field[NUM - 2][NUM - 1] + field[NUM - 2][NUM - 2]
        for j in range(1, NUM-1): # мб начинать с нуля
            cif[0][j] = field[0][j-1] + field[0][j+1] + field[1][j-1] + field[1][j] + field[1][j+1]
            cif[NUM - 1][j] = field[NUM - 1][j-1] + field[NUM - 1][j+1] + field[NUM - 2][j-1] + field[NUM - 2][j] + field[NUM - 2][j+1]
            cif[0][j] *= not field[0][j]
            cif[NUM - 1][j] *= not field[NUM - 1][j]
    
        for i in range(1, NUM-1): # мб начинать с нуля
            cif[i][0] = field[i-1][0] + field[i+1][0] + field[i-1][1] + field[i][1] + field[i+1][1]
            cif[i][NUM - 1] = field[i-1][NUM - 1] + field[i+1][NUM - 1] + field[i-1][NUM - 2] + field[i][NUM - 2] + field[i+1][NUM - 2]
            cif[i][0] *= not field[i][0]
        cif[i][NUM - 1] *= not field[i][NUM - 1]
    
    @staticmethod 
    def fill_square(cif,field,i, j): 
        cif[i][j] = 0
        dif = [-1,0,1]
        for a in dif:
            for b in dif:
                if (a != 0 or b != 0) and field[i][j] != 1: cif[i][j] += field[i+a][j+b]
    def fill_with_zeros(field):
        for i in range(len(field)):
            for j in range(len(field)):
                field[i][j] = 0   


    # Основные методы класса - bombs, hoods, flags, is_win
    def bombs(self): # функция создает минное поле и присваивает его в качестве свойства экземпляру Field, мина = 1, а пустая клетка =0.
        field = []
        for i in range(NUM):
            field.append([])
            for j in range(NUM):
                field[i].append(random.randint(0,1) * random.randint(0,1) * random.randint(0,1) * random.randint(0,1))
        self.bombs = field
    # проверка окрестности. На вход получает поле 1 и 0 (1 - мина, 0 - безопасная клетка), на выход отдает свойство экзепляра, массив из окрестностных оценок.
    def hoods(self): 
        def make_bombs_negative(field, cif):
            for i in range(len(cif)):
                for j in range(len(cif)):
                    if field[i][j] == 1: cif[i][j] = -10
        cif = Field.create_map(NUM)
        field = self.bombs
        Field.fill_borders_corners(cif,field)   
        for i in range(1, NUM - 1): #or this doesnt work
            for j in range(1, NUM - 1):
                Field.fill_square(cif,field,i,j)
        make_bombs_negative(field, cif)
        self.hoods = cif
    def flags_update(self, row, col):
        if self.flags[row][col] == 1: self.flags[row][col] = 0 
        else: self.flags[row][col] = 1 
        if self.flags == self.bombs: 
            for i in range(NUM):
                for j in range(NUM):
                    pygame.draw.rect(self.WIN, yellow, (i * SIZE + OUTLINE, j * SIZE + OUTLINE, SIZE - 2 * OUTLINE, SIZE - 2 * OUTLINE))


        
        



    


        

    

  

        
                
    