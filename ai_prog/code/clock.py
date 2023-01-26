
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

def drawClock():
    for n in range(12):
        t.penup()
        t.setheading(0)
        t.pensize(3)
        t.pencolor('red')
        t.setheading(30 * n)
        t.fd(180)
        t.setheading(30 * n + 90)
        t.pendown()
        t.circle(10)
        t.penup()
        t.home()
  
def draw_second(second):
    t.penup()
    t.home()
    t.pensize(3)
    t.pencolor('orange')    
    t.home()
    t.setheading(90)
    t.rt(second * 6)
    t.pendown()
    t.fd(150)
    t.penup()
    t.home()
    

def draw_min(min):
    t.penup()
    t.home()
    t.pensize(7)
    t.pencolor('purple')    
    t.home()
    t.setheading(90)
    t.rt(min * 6)
    t.pendown()
    t.fd(110)
    t.penup()
    t.home()

def draw_hour(h):
    t.penup()
    t.home()
    t.pensize(12)
    t.pencolor('white')
    t.home()
    t.setheading(90)
    t.rt(h * 30)
    t.pendown()
    t.fd(80)
    t.penup()
    t.home()


while True:
    hour = int(time.strftime('%I'))
    min = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    drawClock()
    draw_hour(hour)
    draw_min(min)
    draw_second(sec)
    ws.update()
    time.sleep(1)
    t.clear()
    

turtle.exitonclick()