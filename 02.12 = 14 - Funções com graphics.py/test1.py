from graphics import *
from one import Forms

window = GraphWin("Shapes", 800, 600)

Forms.triangle(Point(100, 225), Point(250, 375), "#882222", window, "#005555")
Forms.diamond(Point(550, 225), Point(700, 375), "#445577", window, "#228800")

window.getMouse()
window.close()
