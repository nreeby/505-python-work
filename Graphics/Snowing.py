from graphics import *
import random
import math
#remeber to change path for data.txt because it strugals to find it         
with open('C:/Users/nick/Documents/505/Python (4 mini projects)/505-python-work/Graphics/data.txt') as inputfile:
    secondYearResults = [[float(i) for i in line.strip().split()] for line in inputfile]
secondYearResults = [j[0] for j in secondYearResults]
print(secondYearResults)
print (secondYearResults[0])
window = GraphWin("Visualisation", 150, 150)
black=color_rgb(0,0,0)
white=color_rgb(255,255,255)
window.setBackground(black)
#x and y co-ords
co1x=75
co1y=75
#x co-ords
co3=100
co5=135
co7=90
co10=119
co11=126
co13=110
co15=92
co17=87
co19=107
co22=83
co24=97
co26=88
#y co-ords
co2=5
co4=32
co6=40
co8=15
co9=25
co12=45
co14=37
co16=46
co18=31
co20=43
co21=59
co23=61
co25=53
co27=68
#changing the position 
co0=75






#class snowing:
def snowflake():
    for i in range(5):
        #Main
        line1= Line(Point(co1x,co1y),Point(co1x,co2))
        line1.setWidth(4)
        line1.setOutline(white)
        line1.draw(window)
        line2= Line(Point(co1x,co1y),Point(co3,co4))
        line2.setWidth(4)
        line2.setOutline(white)
        line2.draw(window)
        line3= Line(Point(co1x,co1y),Point(co5,co6))
        line3.setWidth(4)
        line3.setOutline(white)
        line3.draw(window)
        #Long Wings
        #Line 1 wings
        #Line 1 outer wings
        line4= Line(Point(co1x,co2),Point(co7,co8))
        line4.setWidth(4)
        line4.setOutline(white)
        line4.draw(window)
        #line 1 inner wings
        line5= Line(Point(co1x,co8),Point(co7,co9))
        line5.setWidth(4)
        line5.setOutline(white)
        line5.draw(window)
        #line 3 wings
        #line 3 outer wings
        line6= Line(Point(co5,co6),Point(co10,co4))
        line6.setWidth(4)
        line6.setOutline(white)
        line6.draw(window)
        #line 3 inner wings
        line7= Line(Point(co11,co12),Point(co13,co14))
        line7.setWidth(4)
        line7.setOutline(white)
        line7.draw(window)
        #Short Wings
        #line 2 
        line8= Line(Point(co15,co16),Point(co17,co18))
        line8.setWidth(4)
        line8.setOutline(white)
        line8.draw(window)
        line9= Line(Point(co15,co16),Point(co19,co20))
        line9.setWidth(4)
        line9.setOutline(white)
        line9.draw(window)
        # Inner ring
        #peak1
        line10= Line(Point(co1x,co21),Point(co22,co16))
        line10.setWidth(4)
        line10.setOutline(white)
        line10.draw(window)
        line11= Line(Point(co22,co23),Point(co22,co16))
        line11.setWidth(4)
        line11.setOutline(white)
        line11.draw(window)
        #peak2
        line12= Line(Point(co22,co23),Point(co24,co25))
        line12.setWidth(4)
        line12.setOutline(white)
        line12.draw(window)
        line13= Line(Point(co26,co27),Point(co24,co25))
        line13.setWidth(4)
        line13.setOutline(white)
        line13.draw(window)
        
        
        
        
        
        
        #To origin
        #x and y co-ords
        global co1x
        co1x=co1x -co0
        global co1y
        co1y=co1y -co0
        #x co-ords
        global co3
        co3=co3 -co0
        global co5
        co5=co5 -co0
        global co7
        co7=co7 -co0
        global co10
        co10=co10 -co0
        global co11
        co11=co11 -co0
        global co13
        co13=co13 -co0
        global co15
        co15=co15 -co0
        global co17
        co17=co17 -co0
        global co19
        co19=co19 -co0
        global co22
        co22=co22 -co0
        global co24
        co24=co24 -co0
        global co26
        co26=co26 -co0
        #y co-ords
        global co2
        co2=co2 -co0
        global co4
        co4=co4 -co0
        global co6
        co6=co6 -co0
        global co8
        co8=co8 -co0
        global co9
        co9=co9 -co0
        global co12
        co12=co12 -co0
        global co14
        co14=co14 -co0
        global co16
        co16=co16 -co0
        global co18
        co18=co18 -co0
        global co20
        co20=co20 -co0
        global co21
        co21=co21 -co0
        global co23
        co23=co23 -co0
        global co25
        co25=co25 -co0
        global co27
        co27=co27 -co0
        
        
        
        
        
        #Rotation
        
        



def snowing():
    snowflake()
snowing()
window.getMouse()