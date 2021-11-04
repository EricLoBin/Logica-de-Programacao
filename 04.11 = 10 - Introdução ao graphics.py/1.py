'''
- Faça um programa que mostre duas linhas. Estas linhas devem fazer o traço de duas diagonais: a principal e a secundária na extensão máxima visível da janela em questão. (Enfim, é o mesmo de fazer um X na janela). 
  A janela deve ser “quadrada”, Utilize: 600 x 600 pixels (colunas x linhas).

'''

from graphics import *

size = 600
window = GraphWin("Window", size, size)

window.setBackground("#ffffff")

line = Line(Point(0, 0), Point(size, size))
line.setFill("#000000")
line.draw(window)
line2 = Line(Point(0, size), Point(size, 0))
line2.setFill("#000000")
line2.draw(window)

window.getMouse()
window.close()