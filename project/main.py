import pygame
from time import sleep
from models import Mell, Food

pygame.init()

W, H = 600, 600

#Базовые настройки
sc=pygame.display.set_mode((W, H)) #pygame.RESIZABLE
pygame.display.set_caption("PeeRusher")

#Базовые цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)

#Установка FPS
FPS = 120
clock = pygame.time.Clock()

#Объявление персонажа
player = Mell(W//2, H//2)

stat1 = pygame.font.SysFont(None, 20)
stat2 = pygame.font.SysFont(None, 64)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or round(player.water) <= 0 or round(player.health) <= 0:
            sc.blit(stat2.render('Игра закончена', 10, RED, BLACK), (140, H//2))
            pygame.display.update()
            sleep(3)
            exit()

    if round(player.water) > 0 and round(player.health) > 0 :
        bt = pygame.key.get_pressed()
        if bt[pygame.K_LEFT]:
            player.move(0, W, H)
        elif bt[pygame.K_RIGHT]:
            player.move(1, W, H)
        elif bt[pygame.K_UP]:
            player.move(2, W, H)
        elif bt[pygame.K_DOWN]:
            player.move(3, W, H)

        sc.fill(BLUE)
        # Cостояния голода и жажды Мелуши
        sc.blit(stat1.render('Жажда: '+str(round(player.water)), 10, WHITE, BLACK), (10, 10))
        sc.blit(stat1.render('Голод: '+str(round(player.health)), 10, WHITE, BLACK), (10, 30))
        # Прорисовка персонажа
        sc.blit(player.imagetemp, player.rect)
        pygame.display.update()
        #Настройка FPS
        clock.tick(FPS)