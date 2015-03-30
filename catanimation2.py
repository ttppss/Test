#doesn't work
import pygame, sys
from pygame.locals import *
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

#set up the window:
windows1 = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("CatAnimation")

WHITE = (255, 255, 255)
cat = pygame.image.load("cat.png")
catx = 10
caty = 10
direction = 'right'

#main game loop:
while True:
    windows1.fill(WHITE)

    if direction == 'right':
        catx = catx + 5
        if catx == 280:
            direction == 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction == 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction == 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction == 'right'

    windows1.blit(cat, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
