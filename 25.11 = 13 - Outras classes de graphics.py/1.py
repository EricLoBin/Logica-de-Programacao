'''
Crie um programa que de forma aleatória crie polígonos na tela a cada vez que o usuário teclar alguma coisa, caso o usuário tecle ESC o programa deve fechar a janela.

Os polígonos devem ter vértices e posições aleatórias, assim como as cores que também devem ser sorteadas.

'''

from graphics import *
from random import randrange
import math

width, height = 800, 600
maxRadius = 100
minRadius = 10

window = GraphWin("Random Polygon", width, height)


def getPoint(x, y, angle, radius):
    radians = 0.01745329 * (angle - 90) # PI/180 * angle
    newPosition = [
        int(radius*math.cos(radians)),
        int(radius*math.sin(radians))
    ]

    return Point(x + newPosition[0], y + newPosition[1])


while True:
    if (window.getKey() == "Escape"):
        break

    verticis = randrange(3, 10)
    x = randrange(0, width)
    y = randrange(0, height)
    radius = randrange(minRadius, maxRadius)
    verticisPosition = [getPoint(x, y, ((360 / verticis)*i), radius) for i in range(verticis)]

    poly = Polygon()
    poly.points = verticisPosition
    poly.setWidth(2)
    poly.setFill(color_rgb(
        randrange(0, 255),
        randrange(0, 255),
        randrange(0, 255)
        ))

    poly.draw(window)

window.close()
