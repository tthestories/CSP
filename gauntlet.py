# # Don't touch the boss code until Vega says you're ready!
for i in range(5):
    boss.moveLeft(3)
    boss.moveRight()
    boss.moveUp()
 
 # Build your Helper items BELOW this line
helper.setPlayer("car")
helper.moveDown()
helper.build("pushable")
helper.moveUp()
helper.moveRight()

for i in range(4):
    helper.build("wall")
    helper.moveDown()

for i in range(2):
    helper.moveDown()
    
for i in range(2):
    helper.build("wall")
    helper.moveRight()

helper.build("spikes")
helper.moveUp()
helper.build("pushable")
helper.moveUp()
helper.build("spikes")
helper.moveLeft()
helper.build("spikes")

for i in range(3):
    helper.moveRight()

for i in range(2):
    helper.moveDown()
    
for i in range(5):
    helper.build("wall")
    helper.moveUp()
