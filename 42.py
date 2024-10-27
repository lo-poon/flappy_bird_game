import pygame as pg
import random
pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

color = (0, 255, 255)
screen.fill(color)

PlayerRect = pg.Rect(10, 300, 60, 60)
RectOfDoom = pg.Rect(600, 350, 100, 350)
RectOfDoom2 = pg.Rect(340, 0, 100, 300)
Bird = pg.image.load("ufo02_by_befree2209_d959hz0-150.png")
Bird = pg.transform.scale(Bird, (60, 60))
OOF = pg.image.load("images.png")
OOF = pg.transform.scale(OOF, (800, 600))

Speed_bird = 10
Speed_pipe = -40
Score = 0
bird_alive = True
while bird_alive == True:
    pg.event.pump()
    #UPDATES
    PlayerRect[1] += Speed_bird
    RectOfDoom[0] += Speed_pipe
    RectOfDoom2[0] += Speed_pipe

    #INPUTS
    L, M, R = pg.mouse.get_pressed()

    #EVENTS(if-statements)
    if L == True:
        PlayerRect[1] -= 80

    if RectOfDoom.collidepoint(-100, 350):
        RectOfDoom[0] += 800
        RectOfDoom[3] = random.randint(10, 400)
        Score += 1


    if RectOfDoom2.collidepoint(-100, 0):
        RectOfDoom2[0] += 800
        RectOfDoom2[3] = random.randint(10, 400)
        Score += 1


    if PlayerRect.colliderect(RectOfDoom):
        bird_alive = False

    if PlayerRect.colliderect(RectOfDoom2):
        bird_alive = False

    if bird_alive == False:
       print("Your score is", Score)

    #DRAWING
    color = (0, 255, 255)
    screen.fill(color)
    color = (0, 255, 255)
    pg.draw.rect(screen, color, PlayerRect)
    color = (0, 255, 0)
    pg.draw.rect(screen, color, RectOfDoom)
    pg.draw.rect(screen, color, RectOfDoom2)
    screen.blit(Bird, (PlayerRect[0], PlayerRect[1]))
    pg.display.flip()

    #CLOCK
    clock.tick(10)

    if bird_alive == False:
       screen.blit(OOF, (0, 0))
       pg.display.flip()
