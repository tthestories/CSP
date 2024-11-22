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
  for i in range(n):
    dinstance = i * 10
    angle = 90
    
    if random.random() < .3:
     door_pos = random.randint(20, dinstance - 20)
     maze.forward(door_pos)
     maze.penup()
     maze.forward(20)
     maze.pendown()
     maze.forward(dinstance - door_pos - 20)
    else:
      maze.forward(dinstance)
      maze.right(angle)
  

drawmaze()

screen.listen()
screen.mainloop()
