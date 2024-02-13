import turtle as t


def rhombus(x, y, a):
    t.fillcolor('green')
    t.begin_fill()
    t.color('green')
    t.up()
    t.setposition(x, y)
    t.down()
    for i in range(2):
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
    for i in range(2):
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
    for i in range(5):
        t.forward(a)
        t.left(72)
        t.forward(a)
        t.right(144)
    t.end_fill()


def square(x, y, a):
    t.fillcolor('red')
    t.begin_fill()
    t.color('red')
    t.up()
    t.setposition(x, y)
    t.down()
    for i in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()


def triangle(x, y, b):
    import math
    t.fillcolor('yellow')
    t.begin_fill()
    t.color('yellow')
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(b)
    t.right(90)
    t.forward(b)
    t.right(135)
    t.forward(b*math.sqrt(2))
    t.right(135)
    t.end_fill()


def circle(x, y, r, c):
    t.fillcolor(c)
    t.begin_fill()
    t.color(c)
    t.up()
    t.setposition(x, y)
    t.down()
    t.circle(r)
    t.end_fill()


def trapeze(x, y, a, h):
    if a > 2 * h:
        t.fillcolor('blue')
        t.begin_fill()
        t.color('blue')
        t.up()
        t.setposition(x, y)
        t.down()
        t.forward(a - 2 * h)
        t.right(45)
        t.forward(h * (2 ** (1/2)))
        t.right(135)
        t.forward(a)
        t.right(135)
        t.forward(h * (2 ** (1/2)))
        t.right(45)
        t.end_fill()



