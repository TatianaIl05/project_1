import turtle as t
def rhombus(x, y, a):
    t.fillcolor('green')
    t.begin_fill()
    t.color('green')
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(135)
    t.forward(a)
    t.right(45)
    t.forward(a)
    t.right(135)
    t.forward(a)
    t.right(45)
    t.end_fill()
def rectangle(x, y, a, b):
    t.fillcolor('pink')
    t.begin_fill()
    t.color('pink')
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.end_fill()
def star(x, y, a):
    t.fillcolor('purple')
    t.begin_fill()
    t.color('purple')
    t.up()
    t.setposition(x, y)
    t.down()
    for i in range (5):
        t.forward(a)
        t.left(72)
        t.forward(a)
        t.right(144)
    t.end_fill()
def round(x, y, r, c):
    t.fillcolor(c)
    t.begin_fill()
    t.color('blue')
    t.up()
    t.setposition(x,y)
    t.down()
    t.circle(r)
    t.end_fill()

