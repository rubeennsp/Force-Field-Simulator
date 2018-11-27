# Ruben Solomon Partono
# In order for this to run, you need to have pygame installed.
# Also, you'll obviously need python installed. Mine is Python 2.7.somethingsomething.
# And you also need Body.py in the same folder as this file, colorfulballs.py
import Body, pygame, sys, random
from Body import Body
from pygame.locals import *


FPS = 30
WINDWIDTH = 800
WINDHEIGHT = 600
WINDSIZE = (WINDWIDTH, WINDHEIGHT)
CAPTION = 'MAKE LOTS OF BALLS!'

#Colors!
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (0,50,0)
MAROON = (100,0,0)

BGCOLOR = MAROON
CLICKCOLOR = WHITE

# This draws a ball (a Body) onto a pygame surface
# the drawinclickcolor is a boolean that tells
# what color the ball should be drawn with
def drawbody(surface, body, drawinclickcolor):
    if drawinclickcolor:
        xpixel = int(body.xpos *100)
        ypixel = int(body.ypos *100)
        pygame.draw.circle(surface, CLICKCOLOR, (xpixel, ypixel), 5, 0)
    else:
        xpixel = int(body.xpos *100)
        ypixel = int(body.ypos *100)
        pygame.draw.circle(surface, body.color, (xpixel, ypixel), 5, 0)

# This method draws all the balls in a specified ball list to a specified pygame surface
def drawballs(surface, ball_list, drawinclickcolor):
    for ball in ball_list:
        drawbody(surface, ball, drawinclickcolor)

# This method adds a ball (again, a Body object) to a list
def addball(ball_list, position):
    newball = Body(position, [0.0,0.0], [0.0,0.0], 1.0)
    ball_list.append(newball)

# This method adds a ball with random color
def addballrandom(ball_list, position):
    newball = Body(position, [0.0,0.0], [0.0,0.0], 1.0)
    newball.color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    ball_list.append(newball)
    print "ball count: %d balls" %len(ball_list)

# This updates the force done by the click to all balls in a list.
# ispressed is a boolean, telling whether the left mouse button is pressed.
def applyclickforce(ball_list, position, ispressed, strength):
    if ispressed:
        x,y = position
        for ball in ball_list:
            ball.clickforce(strength, x, y)
    else:
        for ball in ball_list:
            ball.clickforce(0, 0, 0)

# Does a vertlet step on all balls in the list
def applyvertlet(ball_list, time_step):
    for ball in ball_list:
        ball.vertletstep(time_step)

# Checks and handles if a ball has collided a boundary
def collide_rect(ball, rectinmeters):
    smallx, smally, width, height = rectinmeters
    bigx = smallx + width
    bigy = smally + height

    if (ball.xpos < smallx and ball.xvel < 0) or (ball.xpos > bigx and ball.xvel>0):
        ball.xvel = -ball.xvel*0.7
    if (ball.ypos < smally and ball.yvel < 0) or (ball.ypos > bigy and ball.yvel>0):
        ball.yvel = -ball.yvel*0.7

# Handles colision for all balls in a list
def bounceballs(ball_list, rectinpixels):
    smallx, smally, width, height = rectinpixels
    smallx = float(smallx)/100.0
    smally = float(smally)/100.0
    width = float(width)/100.0
    height = float(height)/100.0
    boundaryinmeters = (smallx, smally, width, height)

    for ball in ball_list:
        collide_rect(ball, boundaryinmeters)

# Colors all balls in a list with a specific color.
def colorballs(ball_list, color):
    for ball in ball_list:
        ball.color = color

def main():
    mouseposx = 0
    mouseposy = 0
    mousestate = [False, False, False, False, False]
    strength = 1.3

    balls = []

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(WINDSIZE)
    pygame.display.set_caption(CAPTION)
    fpsClock = pygame.time.Clock()

    boundaryinpixels = [0,0,WINDWIDTH, WINDHEIGHT]

    # This is the 'game loop'
    # 3 main things happen in the game loop:
    # 1. Input processing: Input is recorded and handled
    # 2. Update Gamestate: Figure out what changes should be made, depending
    #                      on the current state and the input state
    # 3. Rendering: Stuff is then drawn to a surface, which is then displayed
    while True:
        #This clears the screen. What would happen without this?
        #DISPLAYSURF.fill(BGCOLOR)

        #"""
        # This piece of code skips clearing up the surface if the down arrow is pressed.
        # Hot.
        pressedkeys = pygame.key.get_pressed()
        if not(pressedkeys[K_DOWN]):
            DISPLAYSURF.fill(BGCOLOR)
        #"""

        # input processing:
        for event in pygame.event.get():
            if event.type == QUIT: # <- This checks if the X exit button is clicked
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                x,y = event.pos
                mouseposx = x
                mouseposy = y
            elif event.type == MOUSEBUTTONUP:
                mousestate[event.button - 1] = False
            elif event.type == MOUSEBUTTONDOWN:
                mousestate[event.button - 1] = True
                if event.button == 3: # <- This checks if it's a right click
                    addballrandom(balls, [float(mouseposx)/100.0, float(mouseposy)/100.0])
            elif event.type == KEYDOWN:
                if event.key is K_BACKSPACE:
                    balls = balls[:-1]
                else:
                    addballrandom(balls, [float(mouseposx)/100.0, float(mouseposy)/100.0])

        #updating the gamesate:
        applyclickforce(balls, (mouseposx, mouseposy), mousestate[0], strength)
        bounceballs(balls, boundaryinpixels)
        applyvertlet(balls, 0.1)

        #drawing the gamestate:
        drawballs(DISPLAYSURF, balls, mousestate[0])

        pygame.display.update()

        # This waits a certain time, preventing the game loop to loop as fast
        # as the computer can go.
        fpsClock.tick(FPS)

main()
