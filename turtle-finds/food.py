import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self,width,height,x,y,color):
        super().__init__()
        self.image = pygame.image.load("turtle-finds/assets/worm.png")
        self.image = pygame.transform.scale(self.image,(49,49))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.gridPos = 0

    def setWormPosicao(self,matrix,grid_rect,tela):
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                if matrix[i][j] == 0:
                    self.rect.center = grid_rect[i][j]
                    self.gridPos = (i,j)
                    sprite_group = pygame.sprite.Group()
                    sprite_group.add(self)
                    sprite_group.draw(tela)