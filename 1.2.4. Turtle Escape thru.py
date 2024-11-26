import turtle
import random
import math

screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor("lightblue")
screen.tracer(0)

def drawmaze():
  
  maze = turtle.Turtle()
  maze.speed(2)
  maze.color("black")
  maze.pensize(3)
  
  n = 30
  step = 17
  angle = 90
  for i in range(n):
    distance = i * step + step * 2
    door_pos = random.randint(step, distance - step)
    maze.forward(door_pos)
    randomind  = random.randint(1,2)
    if randomind == 2:
      maze.penup()
      maze.forward(step)
      maze.pendown()
      maze.right(angle)
      maze.forward(30)
      maze.backward(30)
      maze.left(angle)
    elif randomind == 1:
      maze.right(angle)
      maze.forward(30)
      maze.backward(30)
      maze.left(angle)
      maze.penup()
      maze.forward(step)
      maze.pendown()
    
    maze.forward(distance - door_pos - step)
    maze.right(angle)

drawmaze()

screen.listen()
screen.mainloop()
