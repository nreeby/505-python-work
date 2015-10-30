from graphics import *
import random
import time
import itertools
#remeber to change path for data.txt because it strugals to find it         
with open('/Users/nreeby/Documents/505-python-work/Graphics/data.txt') as inputfile:
    secondYearResults = [[float(i) for i in line.strip().split()] for line in inputfile]
secondYearResults = [j[0] for j in secondYearResults]
print(secondYearResults)
window = GraphWin("Visualisation", 1000, 1000)
window.setBackground(color_rgb(0,0,0))
r=350
rr=350
size=33.33
speed=0
allballs=[]
ballzspeed=[]
counter= 500
def balls():
    x=random.randint(0,1000)
    y=random.randint(0,700)
    ball = Circle(Point(x,y), rr)
    ball.setFill(color_rgb(size,size,size))
    allballs.append(ball)
    ballzspeed.append(speed)
    ball.draw(window)
    #for i in range(6500):
        #ball.move(0,speed)
def change():
    global size
    size=random.choice(secondYearResults)
    print(size)
    global speed
    speed=0.05*size
    print(speed)
    global rr
    rr= (r/100)*size
    print(rr)
    balls()
    global counter
    counter = 500
def draw_ballz():
    for ballz,spd in itertools.izip(allballs, ballzspeed):
        ballz.move(0,spd)
        global counter
        counter = counter-1
        if (counter == 0):
            change()
change()
while True:draw_ballz()
window.getMouse()