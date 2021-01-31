import pygame

class Mell(pygame.sprite.Sprite):
    #Показатели персонажа
    water = 100.0 
    health = 10.0
    speed = 2

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Melushas.png").convert_alpha()
        self.imageright = pygame.image.load("images/MellRL.png").convert_alpha()
        self.imageleft = pygame.transform.flip(self.imageright, 1, 0)
        self.imageup = pygame.image.load("images/MellUp.png").convert_alpha()

        self.imagetemp = self.image
        self.rect = self.imagetemp.get_rect(center=(x,y))

    def move(self, vector, W, H):
        self.health -= 0.01
        self.water -= 0.1
        if vector == 0:
            self.imagetemp = self.imageleft
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.rect.x = 0
        elif vector == 1:
            self.imagetemp = self.imageright
            self.rect.x += self.speed
            if self.rect.x > W-self.rect.width:
                self.rect.x = W-self.rect.width
        elif vector == 2:
            self.imagetemp = self.imageup
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
        elif vector == 3:
            self.imagetemp = self.image
            self.rect.y += self.speed
            if self.rect.y > H-self.rect.height:
                self.rect.y = H-self.rect.height
    
    #На случай, если игрок бездействует
    def think(self):
        self.health -= 0.001

    def feed(self, Id):
        if Id == 0:
            self.water += 25
        elif Id == 1:
            self.health += 3

class Food(pygame.sprite.Sprite):
    def __init__(self, x , y, Id, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y)) 
        self.Id = Id
        self.add(group)  
