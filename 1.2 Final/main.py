import turtle as trtl
race = trtl.Turtle()

#setup screen stuff
screenh = 159
screenw = 318
wn = trtl.Screen()
wn.setup(width=screenw, height=screenh)
wn.bgpic("Racetrack2.png")

#car setup to start
race.penup()
race.goto(50,40)
race.color("pink")
race.setheading(180)

#car values
speed = 0
max_speed = 1.6
acceleration = 0.5
brake_speed = 1.5
turn_rate = 6

#car functions, taking values set above and making them do stuff
def accelerate():
  global speed
  if speed < max_speed:
    speed += acceleration

def brake():
  global speed
  speed = max(speed - brake_speed, 0)
  
def turn_left():
  race.left(turn_rate)

def turn_right():
  race.right(turn_rate)
  
#keybinds
wn.listen()
wn.onkey(accelerate, "Up")
wn.onkey(brake, "Down")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")

#main loop and boundy settings
while True:
  race.forward(speed)
  
  if race.xcor() > 159 or race.xcor() < -159:
    race.setx(-race.xcor())
  if race.ycor() > 100 or race.ycor() < -100:
    race.sety(-race.ycor())
  
  if speed > 0:
    speed -= 0.05
  elif speed <0:
    speed += 0.05
  speed = max(min(speed, max_speed), -max_speed/2)
  

wn.mainloop() 
