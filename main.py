import pygame
from pygame.locals import *
from sys import exit
import numpy as np

"""
n - liczba krzywych Beizera (punkty kontrolne)
for (l = 0; l < liczba krzywych
    for( t = 0; t <= 1; t += 0.001)
        Px(t)
        Py(t) => z wzoru
        print (Px, Py)

Bezier curves lecture - YouTube
"""

pygame.init()
screen = pygame.display.set_mode((1200, 600))

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    p0 = 450,200
    p1 = 450,400
    p2 = 500,300

    p3 = 600,200
    p4 = 600,400
    p5 = 350,300

    p6 = 400,200
    p7 = 400,400

    screen.fill(0)
    for p in [p0, p1, p2, p3, p4, p5, p6, p7]:
        pygame.draw.circle(screen, (255, 255, 255), p, 2)
    for t in np.arange(0, 1, 0.001):
        px0 = p0[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p2[0] + p1[0] * t ** 2
        py0 = p0[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p2[1] + p1[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px0, py0, 1, 1))

        px1 = p3[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[0] + p4[0] * t ** 2
        py1 = p3[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[1] + p4[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px1, py1, 1, 1))

        px2 = p0[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[0] + p1[0] * t ** 2
        py2 = p0[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[1] + p1[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px2, py2, 1, 1))

        px3 = p6[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[0] + p7[0] * t ** 2
        py3 = p6[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[1] + p7[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px3, py3, 1, 1))

    pygame.display.update()

pygame.quit()
exit()
