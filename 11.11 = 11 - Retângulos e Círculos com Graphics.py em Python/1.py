'''
Faça um programa que desenhe três quadrados pintados por completo de Verde, Amarelo e Azul e que sejam perfeitamente distribuídos em uma linha horizontal fictícia no meio da janela (metade). Cada quadrado deve ter tamanho de 50 pixels de lado.
O tamanho da janela deve ser 600 x 600.

'''

from graphics import *

width, height = 600, 600

window = GraphWin("window", width, height)

def drawSquare(window, x, y, size, color):
    square = Rectangle(Point(x-(size/2), y+(size/2)), Point(x+(size/2), y-(size/2)))
    square.setFill(color)
    square.draw(window)

colors = ["Green", "Yellow", "Blue"]

for i, color in enumerate(colors):
    drawSquare(window, (width/3)*(i+0.5), height/2, 50, color)

window.getMouse()
window.close()
