import turtle
t = turtle.Turtle()
t.color('red')
t.shape('circle')
t.right(90)
t.forward(105)
t.left(90)
t.forward(15)
t.left(90)
t.forward(130)
t.left(150)
t.forward(30)
t.left(120)
t.up()
t.forward(20)
t.down()
for way in range(0, 2):
    t.right(90)
    t.forward(130)
    t.left(150)
    t.forward(30)
    t.left(30)
    t.forward(105)
    t.right(90)
    t.back(15)
    t.up()
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.down()

t.up()
t.forward(20)
t.shape("blank")
turtle.done()
    
    