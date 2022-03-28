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
"""

pygame.init()
screen = pygame.display.set_mode((1200, 600))

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    # Pierwsze K
    p0 = 450,200
    p1 = 450,400

    p3 = 525,200
    p4 = 525,400

    p6 = 425,200
    p7 = 425,400

    p16 = 575,200
    p17 = 575,400

    # Drugie K
    p8 = 700,200
    p9 = 700,400

    p11 = 675,200
    p12 = 675,400

    p14 = 775,200
    p15 = 775,400

    p21 = 825,200
    p22 = 825,400

    # Punkty Kontrolne
    p2 = 450,300
    p5 = 375,300
    p10 = 700,300
    p13 = 675,300
    p19 = 425,300
    p20 = 625,300
    p23 = 625,300
    p24 = 440,200
    p18 = 440,400
    p25 = 680,200
    p26 = 680,400
    p27 = 570,200
    p28 = 550,400
    p29 = 800,200
    p30 = 800,400

    screen.fill(0)

    # Krzywe
    for p in [p0, p1, p3, p4, p6, p7, p8, p9, p11, p12, p14, p15, p16, p17, p21, p22]:
        pygame.draw.circle(screen, (0, 0, 255), p, 2)

    # Punkty Kontrolne
    for p in [p2, p5, p10, p13, p19, p20]:
        pygame.draw.circle(screen, (255, 0, 0), p, 2)

    for t in np.arange(0, 1, 0.001):
        # Pierwsze K
        px = p6[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p19[0] + p7[0] * t ** 2
        py = p6[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p19[1] + p7[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p0[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p2[0] + p1[0] * t ** 2
        py = p0[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p2[1] + p1[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p3[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[0] + p4[0] * t ** 2
        py = p3[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[1] + p4[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p16[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[0] + p17[0] * t ** 2
        py = p16[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p5[1] + p17[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p6[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p24[0] + p0[0] * t ** 2
        py = p6[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p24[1] + p0[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p7[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p18[0] + p1[0] * t ** 2
        py = p7[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p18[1] + p1[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p3[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p27[0] + p16[0] * t ** 2
        py = p3[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p27[1] + p16[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p4[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p28[0] + p17[0] * t ** 2
        py = p4[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p28[1] + p17[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        # Drugie K
        px = p11[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p13[0] + p12[0] * t ** 2
        py = p11[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p13[1] + p12[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p8[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p10[0] + p9[0] * t ** 2
        py = p8[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p10[1] + p9[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p14[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p20[0] + p15[0] * t ** 2
        py = p14[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p20[1] + p15[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p21[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p23[0] + p22[0] * t ** 2
        py = p21[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p23[1] + p22[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p11[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p25[0] + p8[0] * t ** 2
        py = p11[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p25[1] + p8[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p12[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p26[0] + p9[0] * t ** 2
        py = p12[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p26[1] + p9[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p14[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p29[0] + p21[0] * t ** 2
        py = p14[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p29[1] + p21[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

        px = p15[0] * (1 - t) ** 2 + 2 * (1 - t) * t * p30[0] + p22[0] * t ** 2
        py = p15[1] * (1 - t) ** 2 + 2 * (1 - t) * t * p30[1] + p22[1] * t ** 2
        pygame.draw.rect(screen, (255, 255, 255), (px, py, 1, 1))

    pygame.display.update()

pygame.quit()
exit()
