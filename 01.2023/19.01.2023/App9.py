import turtle


def square():
    tt.goto(200, 200)
    tt.pendown()
    for i in range(4):
        tt.forward(100)
        tt.right(90)
    tt.penup()


def circle():
    tt.goto(200, -200)
    tt.pendown()
    tt.circle(80)
    tt.penup()


def triangle():
    tt.goto(-200, -200)
    tt.pendown()
    tt.right(60)
    tt.forward(100)
    tt.right(120)
    tt.forward(100)
    tt.right(120)
    tt.forward(100)
    tt.penup()


def rectangle():
    tt.goto(-200, 200)
    tt.pendown()
    tt.forward(100)
    tt.right(90)
    tt.forward(200)
    tt.right(90)
    tt.forward(100)
    tt.right(90)
    tt.forward(200)
    tt.right(90)
    tt.penup()


def rhombus():
    tt.goto(0, 0)
    tt.pendown()
    tt.forward(200)
    tt.right(60)
    tt.forward(100)
    tt.right(120)
    tt.forward(200)
    tt.right(60)
    tt.forward(100)
    tt.right(120)
    tt.penup()


tt = turtle.Turtle()
tt.shape("turtle")
tt.penup()
for j in range(4):
    n = input().lower()
    if n == 'круг':
        circle()
    elif n == 'квадрат':
        square()
    elif n == 'прямоугольник':
        rectangle()
    elif n == 'треугольник':
        triangle()
    elif n == 'ромб':
        rhombus()
turtle.exitonclick()
