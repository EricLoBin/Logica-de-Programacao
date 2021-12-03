'''
Crie uma função e teste a mesma para que dado os parâmetros ou argumentos: ponto superior esquerdo e o ponto inferior direito (que formam um retângulo “virtual”) desenhe dentro desse retângulo virtual um triângulo.

Crie uma função e teste a mesma para que dado os parâmetros ou argumentos: ponto superior esquerdo e o ponto inferior direito (que formam um retângulo “virtual”) desenhe um losango dentro desse retângulo “virtual”.

'''

from graphics import *

window = GraphWin("Triangle function", 800, 600)

class Forms:
    def triangle(p1, p2, color, window, color_line="#000000"):
        a, b, c = Point(p1.x, p2.y), Point(((p2.x-p1.x)/2)+p1.x, p1.y), p2
        tri = Polygon(a, b, c)
        tri.setFill(color)
        tri.setOutline(color_line)
        tri.setWidth(5)
        tri.draw(window)
        return tri

    def diamond(p1, p2, color, window, color_line="#000000"):
        a, b, c, d = Point(((p2.x-p1.x)/2)+p1.x, p1.y), Point(p2.x, ((p2.y-p1.y)/2)+p1.y), Point(((p2.x-p1.x)/2)+p1.x, p2.y), Point(p1.x, ((p2.y-p1.y)/2)+p1.y)
        dia = Polygon(a, b, c, d)
        dia.setFill(color)
        dia.setOutline(color_line)
        dia.setWidth(5)
        dia.draw(window)
        return dia

Forms.triangle(Point(100, 225), Point(250, 375), "#882222", window, "#005555")
Forms.diamond(Point(550, 225), Point(700, 375), "#445577", window, "#228800")

window.getMouse()
window.close()
