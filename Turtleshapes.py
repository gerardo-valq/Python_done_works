# February 06, 2016
# Gerardo Arturo Valderrama Quiroz A01374994
# Angeles Rodriguez Hernandez A01173339
# Omar Rodrigo Orendain Romero A01374568
# Turtle figures

#Start

#Import turtle
from turtle import *

#Assigning a speed
speed ("normal")

#    ----FIRST FIGURE WINDMILL----

#Assign a counter
counter = 0

 #Using While structure
while counter != 6:
    #Instructions
    forward(100)
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)    
    right (90)
    forward (95)
    right (120)
    counter = counter + 1


#Moving to another figure
forward(100)
penup()
forward(100)
pendown()

#    -----SECOND FIGURE SQUARES -----
#Assign a counter
counter2 = 0

#Assign a variable
figside = 25

#Using While structure
while counter2 != 5:
    #Instructions
    forward(figside)
    left(90)
    forward(figside)
    left(90)
    forward(figside)
    left(90)
    forward(figside)
    left(90)
    figside = figside + 25
    counter2 = counter2 + 1 



#Moving to another figure

penup()
backward(400)
pendown()

#     -----THIRD FIGURE CROSS-----

#Assigning "counter"
counter = 0

#Using while structure
while counter != 4:
    #Instructions
    left (90)
    forward (50)
    left (90)
    forward (50)
    right (90)
    forward (50)
    counter = counter + 1


#Finish turtle
done()

#END
























