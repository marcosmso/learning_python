from turtle import Turtle, Screen, colormode
from random import choice, randint

colors = ["CornFlowerBlue", "IndianRed","DeepSkyBlue","SlateGray"]
pen = Turtle()
pen.shape('turtle')
screen = Screen()

def drawDashedSquare(pen):
  for i in range(4):
    for j in range(10):
      pen.forward(10)
      pen.pendown()
      pen.forward(10)
      pen.penup()
    pen.right(90)

def drawPolygon(pen, num_sides, side_length):
  rotate_angle = 360 / num_sides
  for _ in range(num_sides):
    pen.forward(side_length)
    pen.right(rotate_angle)

def randomColor():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  return (r, g, b)
# for shape_side_n in range(3, 11):
#   pen.color(choice(colors))
#   drawPolygon(pen, shape_side_n, 50)

directions = [0,90,180,270]

colormode(255)
pen.pensize(15)
pen.speed("fastest")

for _ in range(100): 
  pen.color(randomColor())
  pen.setheading(choice(directions))
  pen.forward(30)

screen.exitonclick()