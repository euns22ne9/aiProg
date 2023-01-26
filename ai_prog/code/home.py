import turtle

t = turtle.Turtle()
t.pensize(3)
t.speed(5)

# 지붕 그리기
def drawRoof():
    t.penup()
    t.pencolor('red')
    t.pendown()
    t.forward(100 * (3 ** (1/2)))
    t.setheading(150)
    t.forward(200)
    t.setheading(210)
    t.forward(200)
    t.home()
    t.penup()

# 창문 그리기
def drawWin(x):
    t.penup()
    t.pencolor('green')
    t.goto(-25 + x, -90)
    t.pendown()
    for n in range(4):
        t.setheading(n * 90)
        t.forward(50)
    t.penup()
    t.setheading(0)
    t.forward(25)
    t.setheading(90)
    t.pendown()
    t.forward(50)
    t.penup()
    t.setheading(180)
    t.goto(25 + x, -65)
    t.pendown()
    t.forward(50)
    t.penup()
    
def drawWindows():
    drawWin(0)
    drawWin(100)
    drawWin(-100)

# 문 그리기
def drawDoor():
    t.penup()
    t.home()
    t.goto(20, -200)
    t.pencolor('purple')
    t.pendown()
    t.setheading(90)
    t.forward(60)
    t.setheading(180)
    t.forward(40)
    t.setheading(270)
    t.forward(60)
    t.penup()
    t.home()
    t.setheading(0)
    t.penup()

# 벽 그리기
def drawWall():
    t.penup()
    t.pencolor('orange')
    t.goto(100 * (3 ** (1/2)), 0)
    t.setheading(270)
    t.pendown()
    t.forward(200)
    t.setheading(180)
    t.forward(200 * (3 ** (1/2)))
    t.setheading(90)
    t.forward(200)
    t.penup()

drawRoof()
drawWall()
drawDoor()
drawWindows()

turtle.exitonclick()