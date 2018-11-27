# Ruben Solomon Partono
import Body, pygame, sys
from Body import Body
from pygame.locals import *


FPS = 30
WINDWIDTH = 800
WINDHEIGHT = 600
WINDSIZE = (WINDWIDTH, WINDHEIGHT)
CAPTION = 'Physics!'

#Colors!
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (0,50,0)
MAROON = (100,0,0)

BGCOLOR = MAROON

def drawbody(surface, body):
    xpixel = int(body.xpos *100)
    ypixel = int(body.ypos *100)
    pygame.draw.circle(surface, body.color, (xpixel, ypixel), 5, 0)

def main():
    mouseposx = 0
    mouseposy = 0
    buttonispressed = False

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(WINDSIZE)
    pygame.display.set_caption(CAPTION)
    fpsClock = pygame.time.Clock()

    abody = Body([3.0,2.0], [0.0,0.0], [0.0,0.0], 1.0)
    bbody = Body([5.0,4.0], [0.0,0.0], [0.0,0.0], 1.0)
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                x,y = event.pos
                mouseposx = x
                mouseposy = y
            elif event.type == MOUSEBUTTONUP:
                buttonispressed = False
            elif event.type == MOUSEBUTTONDOWN:
                buttonispressed = True

        if buttonispressed:
            abody.color = WHITE
            abody.clickforce(1, mouseposx, mouseposy)
            bbody.color = BLUE
            bbody.clickforce(1, mouseposx, mouseposy)
        else:
            abody.color = BLACK
            abody.clickforce(0, 0, 0)
            bbody.color = DARKGREEN
            bbody.clickforce(0, 0, 0)

        abody.vertletstep(0.1)
        bbody.vertletstep(0.1)
        drawbody(DISPLAYSURF, abody)
        drawbody(DISPLAYSURF, bbody)

        pygame.display.update()
        fpsClock.tick(FPS)

main()
