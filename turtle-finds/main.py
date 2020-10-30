import pygame
import time

from container import Container
from grid import Grid
from turtle import Turtle
from random import randint

screen =  pygame.display.set_mode([720,600])
screen.fill([240, 183, 179])
container = Container()
grid = Grid()
turtle = Turtle(25,25,(92 + 262),(27 + 262),(255,255,255))

sprite_group = pygame.sprite.Group()
sprite_group.add(turtle)

container.draw_container(screen)
grid.draw_grid(screen)

sprite_group.draw(screen)
pygame.display.flip()

while True:
    movement_type = randint(1, 4)
    turtle.move_turtle(str(movement_type))

    if not container.rect.collidepoint(turtle.rect.x, turtle.rect.y):
        if (movement_type == 4):
            turtle.move_turtle("3")
        elif (movement_type == 1):
            turtle.move_turtle("2")
        elif (movement_type == 3):
            turtle.move_turtle("4")
        elif (movement_type == 2):
            turtle.move_turtle("1")

    screen.fill([203, 237, 216])
    container.draw_container(screen)
    grid.draw_grid(screen)
    sprite_group.draw(screen)
    pygame.display.flip()
    time.sleep(0.5)

    event = pygame.event.poll()
    event_string = pygame.event.event_name(event.type)
    
    if event_string == "Quit":
        break