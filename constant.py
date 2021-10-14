import pygame
#RGB
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
yellow = (255, 255, 0)

#SIZE

NUM = 10
RARITY = 1
SIZE = 640 // NUM
OUTLINE = SIZE // 20

            
pic_1 = pygame.transform.scale(pygame.image.load('D:\\python\\s4per\\tiles\\1.png'), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_2 = pygame.transform.scale(pygame.image.load('D:\\python\\s4per\\tiles\\2.png'), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_3 = pygame.transform.scale(pygame.image.load('D:\\python\\s4per\\tiles\\3.png'), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_4 = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\4.png"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_5 = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\5.png"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_6 = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\6.png"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_7 = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\7.png"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_8 = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\8.png"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
pic_9 = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\9.png"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
flag = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\flag.jpg"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
big_van = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\titry.jpg"), (640, 640))
not_van = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\vanya_unflag.jpg"), (SIZE - 2*OUTLINE, SIZE - 2*OUTLINE))
lose = pygame.transform.scale(pygame.image.load("D:\\python\\s4per\\tiles\\losing.jpg"), (640, 640))