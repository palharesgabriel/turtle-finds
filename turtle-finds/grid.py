import pygame

class Grid(object):
    def __init__(self):
        self.xCoordinate = 80
        self.yCoordinate = 15
        self.width = 50
        self.height = 50

    def draw_grid(self, screen):
        for i in range(0, 9):
            for j in range(0, 9):

                pygame.draw.rect(
                screen, 
                (255, 255, 255),
                pygame.Rect(self.xCoordinate,
                            self.yCoordinate, 
                            self.width, 
                            self.height), 
                1)

                self.xCoordinate += 50
            self.xCoordinate = 80
            self.yCoordinate += 50

        self.xCoordinate = 80
        self.yCoordinate = 15
        self.width = 50
        self.height = 50