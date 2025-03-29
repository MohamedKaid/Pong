from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")


paddle =Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

movingUp=False
movingDown=False

def goUp():
    global movingUp
    movingUp=True
    movingPaddle()

def stopUp():
    global movingUp
    movingUp=False
    
def goDown():
    global movingDown
    movingDown=True
    movingPaddle()
    
def stopDown():
    global movingDown
    movingDown=False
    
def movingPaddle():
    if  movingUp:
        paddle.sety(paddle.ycor()+10)
    elif movingDown:
        paddle.sety(paddle.ycor()-10)

screen.listen()
screen.onkeypress(goUp, "Up")
screen.onkeyrelease(stopUp, "Up")
screen.onkeypress(goDown, "Down")
screen.onkeyrelease(stopDown, "Down")


screen.exitonclick()