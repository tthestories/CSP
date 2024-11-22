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
  step = 18
  angle = 90
  for i in range(n):
    dinstance = i * step
    if random.random() < 0.3 and dinstance > 20:
      door_pos = random.randint(step, dinstance-step)
      maze.forward(door_pos)
      maze.penup()
      maze.forward(25)
      maze.pendown()
      maze.forward(dinstance - door_pos - step)
      maze.right(angle)
    else:
      maze.forward(dinstance)
      maze.right(angle)
  

drawmaze()

screen.listen()
screen.mainloop()
