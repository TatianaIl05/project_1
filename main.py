# Case-study #1
# Developers: Ilinykh T., Ukhov S., Loseva E.
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
     :param y: upper left corner coordinate y
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
    :param x: lower left corner coordinate x
    :param y: lower left corner coordinate y
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
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param b: side length of cathetus
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
     :param x: middle low coordinate x
     :param y: middle low coordinate y
     :param r: radius of a circle
     :param c: color of circle
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
     :param a: the biggest side lengths of a trapeze
     :param h: height of trapeze
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
def parallelogram(x, y, a, b):
    '''
     Function, drawing parallelogram.
     :param x: upper left corner coordinate x
     :param y: upper left corner coordinate y
     :param a: first of the side lengths of a parallelogram
     :param b: second of the side lengths of a parallelogram
     :return: None
     '''
    t.fillcolor('green')
    t.begin_fill()
    t.color('green')
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(135)
    t.forward(b)
    t.right(45)
    t.forward(a)
    t.right(135)
    t.forward(b)
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
    t.right(170)
def rabbit_drawing():
    '''
    Function, drawing rabbit.
    :return: None
    '''
    rectangle(-320, 185, 80, 30)
    circle(-340, 180, 10, 'orange')
    t.left(180)
    triangle(-205, 155, 30)
    t.left(90)
    triangle(-240, 270, 80)
    square(-235, 290, 40)
    t.left(90)
    star(-225, 275, 10)
    circle(-185, 260, 5, 'black')
    t.left(135)
    rhombus(-250, 300, 40)
    t.left(135)
    trapeze(-225, 220, 40, 10)
    t.left(90)

def square_drawing():
    '''
     Function, drawing square.
     :return: None
     '''
    t.left(90)
    triangle(-60, 30, 50)
    t.right(90)
    parallelogram(0, 77, 100, 65)
    rectangle(-60, 25, 115, 50)
    square(-60, -70, 35)
    rectangle(-20, -35, 70, 35)
    t.left(180)
    triangle(90, -70, 35)
    t.left(270)
    trapeze(65, -30, 130, 35)
    t.right(90)
    circle(-43, -60, 9, 'orange')
    circle(8, -65, 12, 'black')
    star(70, 5, 8)
def parrot_drawing():
    '''
     Function, drawing parrot.
     :return: None
     '''
    trapeze(-250, -275, 80, 5)
    square(-235, -281, 8)
    square(-210, -281, 8)
    t.left(90)
    rectangle(-238, -265, 55, 37)
    t.right(90)
    t.right(180)
    triangle(-161, -255, 35)
    t.left(180)
    t.right(90)
    triangle(-243, -217, 40)
    t.left(90)
    t.left(20)
    parallelogram(-225, -183, 34, 30)
    t.right(20)
    t.right(45)
    triangle(-195, -180, 10)
    t.left(45)
    circle(-210, -190, 5, 'white')
    circle(-208, -188, 2.5, 'black')
    star(-240, -185, 3)

def dragon_drawing():
    '''
     Function, drawing dragon.
     :return: None
     '''
    square(200, -90, 60)
    t.right(90)
    triangle(195, -60, 30)
    t.left(90)
    t.right(135)
    triangle(260, -100, 25)
    t.left(135)
    parallelogram(280, -70, 28, 24)
    trapeze(210, -15, 60, 10)
    rectangle(210, 0, 40, 10)
    circle(230, 10, 25, 'orange')
    square(187, 25, 15)
    star(215, 40, 3)
    t.left(30)
    triangle(230, 65, 10)
    t.right(30)
    triangle(250, 60, 10)

def fish_drawing():
    '''
     Function, drawing fish.
     :return: None
     '''
    t.right(45)
    square(-65, 220, 50)
    t.left(45)
    t.left(90)
    trapeze(-23, 253, 100, 25)
    t.right(90)
    t.left(45)
    parallelogram(-25, 180, 45, 50)
    t.right(45)
    t.right(45)
    triangle(10, 255, 45)
    t.left(45)
    star(13, 235, 5)
    circle(-75, 212, 8, 'orange')
    t.right(45)
    parallelogram(-90, 240, 15, 13)
    t.left(45)
    t.left(45)
    rectangle(-105, 195, 25, 9)
    t.right(45)

rabbit_drawing()
fish_drawing()
cat_drawing()
mouse_drawing()
square_drawing()
dragon_drawing()
parrot_drawing()
butterfly_drawing()
