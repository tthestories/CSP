import turtle as trtl

# Setup screen
screenh = 159
screenw = 318
wn = trtl.Screen()
wn.setup(width=screenw, height=screenh)
wn.bgpic("Racetrack2.png")

# Player Cars Setup
car1 = trtl.Turtle()
car1.penup()
car1.goto(-100, 40)  # Start position for player 1
car1.color("pink")
car1.setheading(0)

car2 = trtl.Turtle()
car2.penup()
car2.goto(-100, -40)  # Start position for player 2
car2.color("blue")
car2.setheading(0)

# Car values for both cars
speed = 0
max_speed = 1.6
acceleration = 0.5
brake_speed = 1.5
turn_rate = 6

# Car functions
def accelerate(car):
    global speed
    if speed < max_speed:
        speed += acceleration
    car.forward(speed)

def brake(car):
    global speed
    speed = max(speed - brake_speed, 0)
    car.forward(speed)

def turn_left(car):
    car.left(turn_rate)

def turn_right(car):
    car.right(turn_rate)

# Key bindings for player 1
wn.listen()
wn.onkey(lambda: accelerate(car1), "w")
wn.onkey(lambda: brake(car1), "s")
wn.onkey(lambda: turn_left(car1), "a")
wn.onkey(lambda: turn_right(car1), "d")

# Key bindings for player 2
wn.onkey(lambda: accelerate(car2), "Up")
wn.onkey(lambda: brake(car2), "Down")
wn.onkey(lambda: turn_left(car2), "Left")
wn.onkey(lambda: turn_right(car2), "Right")

# Finish line
finish_line = trtl.Turtle()
finish_line.penup()
finish_line.goto(130, 100)  # Top of the screen
finish_line.pendown()
finish_line.goto(130, -100)  # Bottom of the screen
finish_line.hideturtle()

# Scoreboard
score = trtl.Turtle()
score.penup()
score.goto(-140, 80)
score.color("white")
score.hideturtle()
score.write("P1: 0  P2: 0", align="left", font=("Arial", 12, "normal"))

player1_score = 0
player2_score = 0

# Main loop
while True:
    if car1.xcor() > 130:  # Crossed finish line
        player1_score += 1
        reset_race()
    if car2.xcor() > 130:
        player2_score += 1
        reset_race()
    
    # Update score
    score.clear()
    score.write(f"P1: {player1_score}  P2: {player2_score}", align="left", font=("Arial", 12, "normal"))

    # Boundary checks for both cars
    for car in [car1, car2]:
        if car.xcor() > 159 or car.xcor() < -159:
            car.setx(-car.xcor())
        if car.ycor() > 100 or car.ycor() < -100:
            car.sety(-car.ycor())

        # Deceleration if speed > 0 or < 0
        if speed > 0:
            speed -= 0.05
        elif speed < 0:
            speed += 0.05
        speed = max(min(speed, max_speed), -max_speed/2)

def reset_race():
    global speed
    speed = 0
    car1.goto(-100, 40)
    car1.setheading(0)
    car2.goto(-100, -40)
    car2.setheading(0)

wn.mainloop()
