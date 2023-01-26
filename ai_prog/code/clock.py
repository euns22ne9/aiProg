
import turtle
import time

ws = turtle.Screen()
ws.bgcolor('black')
ws.setup(width=600, height=600)
ws.title('Analog Clock')
ws.tracer(0)

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.pensize(5)
t.hideturtle()

def drawClock(h, min, second):
    t.pensize(3)
    for n in range(12):
        t.pencolor('red')
        t.penup()
        t.home()
        t.setheading(0 + 30 * n)
        t.forward(180)
        t.pendown()
        t.circle(20)
        t.penup()
        t.home()
    
    t.penup()
    t.pensize(3)
    t.pencolor('orange')    
    t.home()
    t.setheading(90)
    t.rt(second * 6)
    t.pendown()
    t.fd(150)

    t.penup()
    t.pensize(7)
    t.pencolor('purple')    
    t.home()
    t.setheading(90)
    t.rt(min * 6)
    t.pendown()
    t.fd(110)

    t.penup()
    t.pensize(12)
    t.pencolor('white')
    t.home()
    t.setheading(90)
    t.rt(h * 30)
    t.pendown()
    t.fd(80)

def draw_second(second):
    t.penup()
    t.pensize(3)
    t.pencolor('orange')    
    t.home()
    t.setheading(90)
    t.rt(second * 6)
    t.pendown()
    t.fd(150)
    

def draw_min(min):
    t.penup()
    t.pensize(7)
    t.pencolor('purple')    
    t.home()
    t.setheading(90)
    t.rt(min * 6)
    t.pendown()
    t.fd(110)

def draw_hour(h):
    t.penup()
    t.pensize(12)
    t.pencolor('white')
    t.home()
    t.setheading(90)
    t.rt(h * 30)
    t.pendown()
    t.fd(80)


while True:
    hour = int(time.strftime('%I'))
    min = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    drawClock(hour,min, sec)
    ws.update()
    time.sleep(1)
    t.clear()
    

turtle.exitonclick()