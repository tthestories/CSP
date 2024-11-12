#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.penup()
  active_apple.shape(apple_image)
  wn.update()
  namer()

def fall():
  #print(appletofall," falling")
  apple.clear()
  apple.goto(apple.xcor(),-350)

def namer():
  apple.color("red")
  apple.write("A", font=("Arial",74,"bold"))
 
#-----function calls-----
draw_apple(apple)

wn.onkeypress(fall,"a")

wn.bgpic("background.gif")
wn.listen()
wn.mainloop()
