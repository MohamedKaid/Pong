from turtle import Turtle


class Paddle(Turtle):
    
    def __init__ (self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
        self.movingUp=False
        self.movingDown=False

    def goUp(self):
        self.movingUp=True
        self.movingPaddle()

    def stopUp(self):
        self.movingUp=False
        
    def goDown(self):
        self.movingDown=True
        self.movingPaddle()
        
    def stopDown(self):        
        self.movingDown=False
        
    def movingPaddle(self):
        if  self.movingUp:
            self.sety(self.ycor()+10)
        elif self.movingDown:
            self.sety(self.ycor()-10)


