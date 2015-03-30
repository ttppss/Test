import pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 600
WINDOWHEIGHT = 480
BOXSIZE = 40
BOXGAP = 10
REVEALSPEED = 8

BOARDWIDTHNUM = 10
BOARDHEIGHTNUM = 8
TOPMARGIN = int((WINDOWHEIGHT - BOARDHEIGHTNUM * (BOXSIZE + BOXGAP)) / 2)
SIDEMARTIN = int((WINDOWWIDTH - BOARDWIDTHNUM * (BOXSIZE + BOXGAP)) / 2)
assert BOARDWIDTHNUM * BOARDHEIGHTNUM % 2 == 0, "THE NUMBER OF BOXES SHOULD BE EVEN"

GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLOR = (GRAY, NAVYBLUE, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPE = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLOR) * len(ALLSHAPE) * 2 >= BOARDWIDTHNUM * BOARDHEIGHTNUM, "BOARD IS TOO BIG FOR THE NUMBER OF SHAPES/COLORS DEFINED"

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0
    mousey = 0
    pygame.display.set_caption("demo001")

    mainboard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)
    firstselection = None

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)
    while True:
        mouseClicked == False

        DISPLAYSUR.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)
    


def getRandomizedBoard():
    icon = []
    for color in ALLCOLOR:
        for shape in ALLSHAPE:
            icon.append((color, shape))

def generateRevealedBoxesDate(val):
    revealedBoxes = []
    for i in range(BOARDWIDTHNUM):
        revealedBoxes.append([val] * BOARDHEIGHTNUM)

def startGameAnimation(board):
    
        
