import pygame
from random import randint
from time import sleep
from models import Mell, Food

#Инициализация всех модулей pygame
pygame.init()

#Задержка появления объектов Еда
pygame.time.set_timer(pygame.USEREVENT, 2500)

W, H = 600, 600

#Базовые настройки
sc=pygame.display.set_mode((W, H)) #pygame.RESIZABLE
pygame.display.set_caption("PeeRusher")
pygame.display.set_icon(pygame.image.load("images/Melushas.bmp"))

#Базовые цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DarkGREEN = (0, 100, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)

#Установка FPS
FPS = 120
clock = pygame.time.Clock()

#Объявление персонажа
player = Mell(W//2, H//2)

#Базовые форматы шрифтов
stat1 = pygame.font.SysFont(None, 20)
stat2 = pygame.font.SysFont(None, 64)

#Группа обьектов Еда
food = pygame.sprite.Group()

#Метод создания нового объекта Еда
food_images = ["water.png","corm.png"]
food_surf = [pygame.image.load("images/"+path).convert_alpha() for path in food_images]
def createFood(group):
    indx = randint(0, len(food_surf)-1)
    x = randint(20, W-20)
    y = randint(50, H-20)

    return Food(x, y, indx, food_surf[indx], group)

#Метод кормления
def collideFood():
    for f in food:
        if player.rect.collidepoint(f.rect.center):
            player.feed(f.Id)
            f.kill()

#Добавление первого объекта Еда
createFood(food)

#Основной код
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or round(player.water) <= 0 or round(player.health) <= 0:
            sc.blit(stat2.render('Игра закончена', 10, RED, BLACK), (140, H//2))
            pygame.display.update()
            sleep(3)
            exit()
        elif event.type == pygame.USEREVENT: #Появление новых обьектов Еда
            if len(food) < 20: #ДопУсловие, чтобы слишком много еды не было
                createFood(food)

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
        else:
            player.think()

        sc.fill(DarkGREEN)

        #Контроль кормления
        collideFood()

        #Cостояния голода и жажды Мелуши
        sc.blit(stat1.render('Жажда: '+str(round(player.water)), 10, WHITE, BLACK), (10, 10))
        sc.blit(stat1.render('Голод: '+str(round(player.health)), 10, WHITE, BLACK), (10, 30))

        #Прорисовка объектов Еда
        food.draw(sc)

        #Прорисовка персонажа
        sc.blit(player.imagetemp, player.rect)
        pygame.display.update()

        #Настройка FPS
        clock.tick(FPS)
