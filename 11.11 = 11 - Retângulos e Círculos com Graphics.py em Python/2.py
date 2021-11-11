'''
Faça um programa que desenhe sempre a partir do centro da janela 66 círculos que tenham raio de 3 até 198 pixels (3, 6, 9, 12, …, 198), pulando de 3 em 3. A janela deve ter tamanho 600 x 600

'''

from graphics import *

width, height = 600, 600

window = GraphWin("window", width, height)
window.setBackground("#afafaf")

def drawCircle(window, radius, color):
    circle = Circle(Point(width/2, height/2), radius)
    circle.setOutline(color)
    circle.draw(window)


for i in range(3, 199, 3):
    drawCircle(window, i, color_rgb(0, int(255*(i/198)), int(255*(i/198))))


window.getMouse()
window.close()
