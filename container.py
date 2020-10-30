import pygame

class Container(object):
    def __init__(self):
        self.xCoordinate = 80
        self.yCoordinate = 15
        self.width = 450
        self.height = 450
        self.rect = pygame.Rect(self.xCoordinate, self.yCoordinate, self.width, self.height)

    def draw_container(self, screen):
        pygame.draw.rect(screen, (184, 184, 243), self.rect )