import turtle as t

t.pensize(2)
def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()

t.ht()
t.done()