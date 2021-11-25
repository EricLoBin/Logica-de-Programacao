'''
Crie um programa que faça uma GRID na janela de pequenos quadrados, onde o lado varie de 3 à 9 pixels, a sua escolha, e que sejam pintados um de Azul e outro Vermelho, preenchendo toda a extensão da tela.

'''

from graphics import *

number_of_squares_x = 50
number_of_squares_y = 50
square_size = 9

window = GraphWin("Squares", number_of_squares_x*square_size, number_of_squares_y*square_size)

def create_square(x, y, color):
    square = Rectangle(Point(x, y), Point(x + square_size, y + square_size))
    square.setWidth(0)
    square.setFill(color)
    square.draw(window)

for i in range(number_of_squares_x):
    for j in range(number_of_squares_y):
        create_square(i*square_size, j*square_size, "#ff0000" if ((i + j) % 2 == 0) else "#0000ff")


window.getMouse()
window.close()
