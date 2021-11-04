'''
- Faça um programa que desenhe uma linha reta horizontal no meio da janela, mas que seja pontilhada, esta deve ir da coluna 0 até a 599. 
  Sugestão: Utilize o for para isso. Dica: nem toda coluna deve ter um ponto plotado (para ficar pontilhado). 
  A janela deve ser “quadrada”. Utilize: 600 x 600 pixels (colunas x linhas).

'''

from graphics import *

size = 600
window = GraphWin("Window", size, size)

window.setBackground("#ffffff")

for i in range(0, size, 5):
    point = Point(i, (size/2))
    point.setFill("#000000")
    point.draw(window)

window.getMouse()
window.close()