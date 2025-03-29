from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)


rPaddle= Paddle((370, 0))
lPaddle= Paddle((-370, 0))

ball = Ball()




screen.listen()

# Right paddle movment
screen.onkeypress(rPaddle.goUp, "Up")
screen.onkeyrelease(rPaddle.stopUp, "Up")
screen.onkeypress(rPaddle.goDown, "Down")
screen.onkeyrelease(rPaddle.stopDown, "Down")

# Left paddle movment
screen.onkeypress(lPaddle.goUp, "w")
screen.onkeyrelease(lPaddle.stopUp, "w")
screen.onkeypress(lPaddle.goDown, "s")
screen.onkeyrelease(lPaddle.stopDown, "s")



game_is_on =True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce()
    
screen.exitonclick()