for i in range(5):
    boss.moveLeft(3)
    boss.moveRight()
    boss.moveUp()
 
 # Build your Helper items BELOW this line
helper.setPlayer("car")
for i in range(3):
    helper.moveRight()
    helper.build("rightArrow")
     
for i in range(3):
    helper.moveDown()
    helper.build("wall")

helper.moveDown()
helper.build("spikes")
for i in range (3):
    helper.moveRight()
    helper.build("rightArrow")
    
helper.build("wall")
helper.moveDown()
helper.build("downArrow")
