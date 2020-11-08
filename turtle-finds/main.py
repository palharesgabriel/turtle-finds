import pygame
import time

from container import Container
from grid import Grid
from turtle import Turtle
from rock import  Rock
from food import Food
from random import randint
from astar import aStar

screen =  pygame.display.set_mode([600,480])
screen.fill([203, 237, 216])
container = Container()
grid = Grid()
turtle = Turtle(25,25,(92 + 262),(27+262),(255,255,255))
rock = Rock(25,25,(92 + 262),(27+262),(255,255,255))
food = Food(25,25,(92 + 262),(27+262),(255,255,255))
grid.create_matrix()

sprite_group = pygame.sprite.Group()
sprite_group.add(turtle)

container.draw_container(screen)
grid.draw_grid(screen)

turtle.set_initial_position(8, 8, grid.rectMap)
food.setWormPosicao(grid.matrix, grid.rectMap, screen)
rock.setRockPosicao(grid.matrix, grid.rectMap, screen)

sprite_group.draw(screen)
pygame.display.flip()

terminado = False
while True:
    if terminado == False:
        turtleMov = aStar(turtle.gridPos, food.gridPos, food.matrix)
        for i in turtleMov:
            time.sleep(0.5)
            turtle.move_turtle(str(i))
            if not container.rect.collidepoint(turtle.rect.x, turtle.rect.y):
                if (i == 4):
                    turtle.move_turtle("3")
                elif (i == 1):
                    turtle.move_turtle("2")
                elif (i == 3):
                    turtle.move_turtle("4")
                elif (i == 2):
                    turtle.move_turtle("1")



            screen.fill([203, 237, 216])
            container.draw_container(screen)
            grid.draw_grid(screen)
            sprite_group.draw(screen)
            rock.setRockPosicao(grid.matrix, grid.rectMap, screen)
            food.setWormPosicao(grid.matrix, grid.rectMap, screen)
            pygame.display.flip()
            time.sleep(0.1)
            event = pygame.event.poll()

        terminado = True
        screen.fill([203, 237, 216])
        container.draw_container(screen)
        grid.draw_grid(screen)
        sprite_group.draw(screen)
        rock.setRockPosicao(grid.matrix, grid.rectMap, screen)
        pygame.display.flip()
        time.sleep(0.1)
    time.sleep(1)

    event = pygame.event.poll()
    event_string = pygame.event.event_name(event.type)
    
    if event_string == "Quit":
        break