from time import sleep
import pygame as pg
from random import randint, random
pg.init()

screen = pg.display.set_mode((400, 300), pg.FULLSCREEN)
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
          run = False  
    pg.mouse.set_visible(False)
    screen.fill((0, 0, 0))
    for i in range(randint(1, 60)):
        sleep(0.025)
        pg.draw.circle(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (randint(0, 2000), randint(0, 1300)), randint(1, 100))
    pg.display.flip()
pg.quit() 
