import turtle

s=turtle.Screen().bgcolor('black')
t=turtle.Turtle()
t.speed(0)
t.width(12)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color('red','red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.penup()
t.goto(-30,50)
t.pendown()
t.color("white")
t.right(150)
t.forward(80)
t.right(135)
t.forward(80)
t.back(40)
t.right(90)
t.forward(40)

turtle.exitonclick()
