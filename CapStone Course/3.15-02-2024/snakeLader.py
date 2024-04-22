import turtle
import time
import random

score = 0
high_score = 0
delay = 0.1


wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor("#000117")
wn.setup(width=700, height=700)
wn.tracer(0) 

pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape('square')
pencil.color('white')
pencil.penup()
pencil.hideturtle()
pencil.goto(310,310)
pencil.pendown()
pencil.goto(-310,310)
pencil.goto(-310,-310)
pencil.goto(310,-310)
pencil.goto(310,310)
pencil.penup()


head = turtle.Turtle()
head.speed(0) 
head.shape("square")
head.color('white')
head.penup()
head.goto(0,0)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0) 
food.shape("circle")
food.color('red')
food.penup()
food.goto(0,100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write('Score: 0 High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))


def update_score():
    pen.clear()
    pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font = ('Courier', 24, 'normal'))

def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)

def collision():
    time.sleep(0.5)
    head.goto(0,0)
    head.direction = 'stop'
    for segment in segments:
        segment.hideturtle()
    segments.clear()
    score = 0
    update_score()
    delay = 0.1

wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        collision()

    if head.distance(food) < 20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    move()

    for segment in segments:
        if segment.distance(head) < 10:
            collision()
    time.sleep(delay)

wn.mainloop()