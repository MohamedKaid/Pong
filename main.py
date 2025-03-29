from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)


rPaddle= Paddle((350, 0))
lPaddle= Paddle((-350, 0))




screen.listen()
screen.onkeypress(rPaddle.goUp, "Up")
screen.onkeyrelease(rPaddle.stopUp, "Up")
screen.onkeypress(rPaddle.goDown, "Down")
screen.onkeyrelease(rPaddle.stopDown, "Down")




game_is_on =True
while game_is_on:
    screen.update()
    
screen.exitonclick()