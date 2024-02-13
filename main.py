# Case-study #1
# Developers: Ilinykh T.
#

import turtle as t


def rhombus(x, y, a):
    '''
    Function, drawing rhombus.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a rhombus
    :return: None
    '''
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
    '''
    Function, drawing rectangle.
    :param x: upper left corner coordinate x
    :param y: upper left cirner coordinate y
    :param a: first of the side lengths of a rectangle
    :param b: second of the side lengths of a rectangle
    :return: None
    '''
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
    '''
    Function, drawing star.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a star
    :return: None
    '''
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
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''
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
    '''
    Function, drawing triangle
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param b: leg length of a rectangular triangle
    :return: None
    '''
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
    '''
    Function, drawing circle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param r: radius of a circle
    :param c: colour of a circle
    :return: None
    '''
    t.fillcolor(c)
    t.begin_fill()
    t.color(c)
    t.up()
    t.setposition(x, y)
    t.down()
    t.circle(r)
    t.end_fill()


def trapeze(x, y, a, h):
    '''
    Function, drawing trapeze.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: length of a larger base of trapeze
    :param h: length of a height of trapeze
    :return: None
    '''
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


def cat_drawing():
    '''
    Function, drawing cat.
    :return: None
    '''
    trapeze(180, 270, 200, 50)
    t.right(45)
    triangle(120, 320, 70)
    t.left(180)
    triangle(340, 220, 70)
    t.right(135)
    circle(260, 230, 15, 'white')
    circle(200, 230, 15, 'white')
    circle(265, 235, 10, 'black')
    circle(205, 235, 10, 'black')
    rectangle(195, 210, 70, 90)
    square(210, 125, 40)
    star(217, 145, 10)
    t.right(90)
    triangle(190, 140, 20)
    t.right(90)
    triangle(290, 120, 20)
    t.right(135)
    rhombus(275, 180, 30)
    t.right(45)


def mouse_drawing():
    '''
    Function, drawing mouse.
    :return: None
    '''
    trapeze(-250, -90, 30, 9)
    trapeze(-290, -90, 30, 9)
    rectangle(-295, -45, 60, 40)
    t.left(180)
    triangle(-235, -40, 60)
    t.right(180)
    triangle(-295, 25, 60)
    square(-295, 30, 30)
    triangle(-300, 95, 80)
    circle(-330, 80, 30, 'orange')
    circle(-190, 80, 30, 'orange')
    star(-205, 110, 10)
    star(-340, 110, 10)
    circle(-250, 70, 5, 'black')
    circle(-220, 75, 5, 'black')
    circle(-220, 19, 3, 'black')
    t.left(135)
    rhombus(-325, -75, 20)
    t.right(135)


def butterfly_drawing():
    '''
    Function, drawing butterfly.
    :return: None
    '''
    rectangle(60, -290, 80, 15)
    circle(45, -305, 9, 'orange')
    t.left(155)
    rectangle(25, -300, 80, 15)
    t.right(10)
    rectangle(-55, -260, 60, 4)
    t.right(10)
    rectangle(-51, -255, 60, 4)
    star(-110, -225, 5)
    star(-95, -210, 5)
    t.left(35)
    trapeze(60, -285, 100, 30)
    t.right(180)
    square(0, -240, 40)
    triangle(-37, -192, 40)
    t.left(180)
    triangle(40, -200, 80)
    rhombus(97, -255, 50)


cat_drawing()
mouse_drawing()
butterfly_drawing()

