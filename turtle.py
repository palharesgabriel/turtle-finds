import pygame

class Turtle(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        
        self.image = pygame.image.load("turtle.png")
        self.image = pygame.transform.scale(self.image,(49,49))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def move_turtle(self, movementType):
        count = 0
        # UP
        if movementType == "1":
            while(count < 50):
                self.rect.y -= 10
                count += 10
        # DOWN
        elif movementType == "2":
            while (count < 50):
                self.rect.y += 10
                count += 10
        # RIGHT
        elif movementType == "3":
            while (count < 50):
                self.rect.x += 10
                count += 10
        # LEFT
        elif movementType == "4":
            while (count < 50):
                self.rect.x -= 10
                count += 10