
import turtle
import time

ws = turtle.Screen()
ws.bgcolor('black')
ws.setup(width=600, height=600)
ws.title('Analog Clock')
#ws.tracer(0)

t = turtle.Turtle()
t.shape('turtle')
t.speed(300)
t.pensize(5)
t.hideturtle()

def drawMin():
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

'''
t.pendown()
while True:
    for n in range(60):
        t.pencolor('orange')    
        t.setheading(90 - 6 * n)
        t.forward(150)
        t.pencolor('white')
        t.setheading(270 - 6 * n)
        t.home()
'''
'''
while True:
    hour = int(time.strftime('%I'))
    min = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    t.pencolor('orange')    
    t.setheading(90 - 6 * sec)
    t.forward(150)
    t.pencolor('white')
    t.setheading(270 - 6 * sec)
    t.home()
'''

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

t.pendown()
while True:
    drawMin()
    hour = int(time.strftime('%I'))
    min = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    print(hour, min, sec, sep=":")
    draw_hour(hour)
    draw_min(min)
    draw_second(sec)
    ws.update()
    time.sleep(1)
    t.clear()
    

turtle.exitonclick()