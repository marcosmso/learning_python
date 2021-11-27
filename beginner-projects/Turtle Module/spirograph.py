from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)
pen = Turtle()
pen.shape('turtle')
screen = Screen()

def randomColor():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  return (r, g, b)

def drawSpirograph(size_of_gap):
  for _ in range(int(360/size_of_gap)):
    pen.color(randomColor())
    pen.circle(100)
    pen.setheading(pen.heading() + size_of_gap) 

pen.pensize(1)
pen.speed("fastest")
drawSpirograph(10)

screen.exitonclick()