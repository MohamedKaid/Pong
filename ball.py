from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove=10
        self.ymove=10 
        
    
    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx,newy)
        
    def bounce(self):
        self.ymove*= -1
    
    def hitbounce(self):
        self.xmove*= -1