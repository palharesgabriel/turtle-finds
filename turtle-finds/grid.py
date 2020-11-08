import pygame

class Grid(object):
    def __init__(self):
        self.x = 80
        self.y = 15
        self.width = 50
        self.height = 50
        self.matrix = []
        self.rectMap = []

    def create_matrix(self):
        line = []
  
        for i in range(0, 9):
            for j in range(0, 9):
                if i == 0 and j == 0:
                    line.append(0)
                elif i == 7 and j == 8:
                    line.append(3)
                elif i == 7 and j == 7:
                    line.append(3)
                elif i == 6 and j == 7:
                    line.append(3)
                elif i == 5 and j == 5:
                    line.append(3)
                elif i == 4 and j == 4:
                    line.append(3)
                elif i == 1 and j == 1:
                    line.append(3)
                elif i == 2 and j == 1:
                    line.append(3)
                elif i == 3 and j == 5:
                    line.append(3)
                else:
                    line.append(2)
            self.matrix.append(line)
            line = []

    def draw_grid(self,tela):
        line_frame = []
        for i in range(0,len(self.matrix)):
            for j in range(0, len(self.matrix)):
                pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(self.x,self.y,self.width,self.height),1)
                line_frame.append((self.x+25,self.y+25))
                self.x += 50
            self.x = 80
            self.y += 50
            self.rectMap.append(line_frame)
            line_frame = []

        self.x = 80
        self.y = 15
        self.width = 50
        self.height = 50