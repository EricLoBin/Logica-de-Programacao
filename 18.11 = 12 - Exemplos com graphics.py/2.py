'''
Faça um programa que desenhe um túnel fictício (da mesma forma que foi feito para o túnel de círculos), porém que seja feito de quadrados em uma janela.

'''

from graphics import *

margin = 30
square_size = 95
square_spacing = 6
number_of_squares = 60

window = GraphWin("Square tunnel", (number_of_squares*square_spacing) + square_size + (margin*2), (number_of_squares*square_spacing) + square_size + (margin*2))

def create_square(x, y, color):
    square = Rectangle(Point(x, y), Point(x + square_size, y + square_size))
    square.setWidth(2)
    square.setOutline(color)
    square.draw(window)

for i in range(number_of_squares):
    create_square((i*square_spacing) + margin, (i*square_spacing) + margin, color_rgb(0, 0, (100 + int(155 * (i/number_of_squares)))))


window.getMouse()
window.close()
