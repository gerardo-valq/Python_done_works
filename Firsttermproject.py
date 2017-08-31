
# February 13, 2016
# Angeles Rodriguez Hernandez A01173339
# Gerardo Arturo Valderrama Quiroz A01374994
# Omar Rodrigo Orendain Romero A01374568
# Alfredo Alarcon Valencia A01375414

# Group 4
# Project

# START
# Import Turtle Library
from turtle import *

#Assigning a speed
speed(10)

# Color Settings
bgcolor("#160D50")

fillcolor ("#141417")


#        ---------Configurating Background---------

# Back Buildings
pencolor("#001069")
penup()
setpos(-700, -90)
pendown()


#Function definition back buildongs
def back_build ():

    left (90)
    forward (300)
    right (90)
    forward (40)
    left(90)
    forward (20)
    right (90)
    forward(27)
    right (90)
    forward (20)
    left (90)
    forward (40)
    right (90)
    forward (300)
    left(90)
    forward (5)
    left (90)
    forward (300)
    right (50)
    forward (60)
    right (135)
    forward(40)
    left(135)
    forward (60)
    right (130)
    forward (340)
    left (90)
    forward (10)
    left (90)
    forward (320)
    right (90)
    forward (50)
    right (90)
    forward (320)
    left (90)
    forward (2)
    left (90)
    forward (250)
    right (90)
    forward (50)
    right (90)
    forward (250)
    left (90)
    forward (2)
    left (90)
    forward (180)
    right (90)
    forward (50)
    right (90)
    forward (180)
    left (90)
    forward (2)
    left (90)
    right (90)
    forward (1)
    
#Function use back buildings    
for counter in range (4):
    fillcolor ("#001069")
    begin_fill()
    back_build()
    end_fill()

#Function definition back buildings 2

pencolor("#2F365E")
penup()
setpos(-700, -100)
pendown()

def back_build2 ():

    left (90) 
    forward (300)
    right (90)
    forward (50)
    right (90)
    forward (300)
    left (90)
    forward (2)
    left (90)
    forward (160)
    right (90)
    forward (50)
    right (90)
    forward (160)
    left (90)
    forward (2)
    left (90)
    forward (230)
    right (90)
    forward (50)
    right (90)
    forward (230)
    left (90)
    forward (2) 
    left (90)
    forward (300)
    right (90)
    forward (50)
    right (90)
    forward (300)
    left (90)
    forward (2)
    left (90)
    forward (160)
    right (90)
    forward (50)
    right (90)
    forward (160)
    left (90)
    forward (2)
    left (90)
    right (90)
    forward (1)

#Function use back buildings 2
for counter in range (7):
    fillcolor ("#2F365E")
    begin_fill()
    back_build2()
    end_fill()



#          --------Building primary buildings-------
#New color adjustments
pencolor("#141417")
fillcolor ("#141417")

# Function Definition Buildings
def buildings (lenght):
    forward (80)
    left(90)
    forward(lenght + 100)
    left(90)
    forward(80)
    left(90)
    forward(lenght + 100)
    left (90)

# Function Use Buildings
lenght = 100
penup()
setpos(-650, -100)
pendown()
for counter in range (2):
    begin_fill()
    buildings (lenght)
    forward (90)
    lenght = lenght + 40
    end_fill()
    
    

# Function Definition Skyscrapers
def skyscrapers ():
    forward (100)
    left (90)
    forward(400)
    left(90)
    forward (100)
    left (90)
    forward (400)
    left (90)
    

# Function Use Skyscrapers
for counter in range (1):
    begin_fill()
    forward (10)
    skyscrapers ()
    end_fill()

# Function Definition of the tallest Skyscrapers
def tall_skyscraper():
    forward (100)
    left (90)
    forward(475)
    left(90)
    forward (100)
    left (90)
    forward (475)
    left (90)


# Function Use tallest Skyscrapers
for counter in range (1):
    begin_fill()
    forward (120)
    tall_skyscraper()
    end_fill()

# Function Definition asimetric building
def asi_building ():
    forward (90)
    left (90)
    forward (200)
    left(90)
    forward (30)
    right(90)
    forward(20)
    left(90)
    forward(30)
    left(90)
    forward(20)
    right(90)
    forward(30)
    left(90)
    forward(200)
    left(90)

# Function Use asimetric building
for counter in range (1):
    begin_fill()
    forward(105)
    fillcolor("#10101A")
    asi_building()
    end_fill()
    
# Function Definition asimetric building 2
def asi_build2():
    forward(100)
    left(90)
    forward(210)
    left(120)
    forward(100)
    left(60)
    forward(160)
    left(90)

# Function Use asimetric building 2
for counter in range(1):
    begin_fill()
    forward(80)
    asi_build2()
    end_fill()
    

# Function Definition Street
def street():
    right (120)
    forward (300)
    left(120)
    forward (400)
    left(120)
    forward (300)
    left (60)
    forward(45)


# Function Use Street
for counter in range (1):
    fillcolor("#3D3D4F")
    begin_fill()
    forward(70)
    street()
    end_fill()


# Function Definition Line of the street
def line ():
    left(100)
    forward(300)
    right(100)
    forward(110)
    right(100)
    forward(300)
    right(80)

# Function Use Line of the street
for counter in range (1):
    fillcolor("#FAFCFC")
    begin_fill()
    line()
    end_fill()

#Move the pen
penup ()
forward (50)
pendown ()

# Function use asimetric building
for counter in range (1):
    fillcolor ("#141417")
    begin_fill()
    asi_building()
    end_fill()
    forward (90)

# Function definition taller asimetric building 
def asi_build3 ():
    forward (90)
    left (90)
    forward (320)
    left (90)
    forward (15)
    right (90)
    forward (30)
    left (90)
    forward (15)
    right (90)
    circle(15,180)
    right (90)
    forward (15)
    left(90)
    forward (30)
    right(90)
    forward(15)
    left (90)
    forward (320)
  
    
# Function use taller asimetric building
fillcolor ("#141417")
begin_fill()
penup()
forward (20)
pendown ()
asi_build3()
end_fill()

# Move the pen
penup ()
left (90)
forward (110)
pendown ()

# Function use skyscraper
fillcolor ("#141417")
begin_fill()
skyscrapers()
end_fill()
penup()
forward (120)
pendown ()

# Function definition taller asimetric building 2
def asi_build4 ():

    forward (100)
    left (90)
    forward (320)
    left (45)
    forward (25)
    right (45)
    forward (30)
    left (60)
    forward(27)
    left (60)
    forward (27)
    left (60)
    forward (30)
    right (45)
    forward (25)
    left (45)
    forward (320)
    left (90)


# Function use taller asimetric building 2
fillcolor ("#141417")
begin_fill()
asi_build4 ()
end_fill()
forward (80)


# Function use asimetric building 2
fillcolor ("#141417")
begin_fill()
asi_build2 ()
end_fill()
forward (90)


# Function use skyscraper
fillcolor ("#141417")
begin_fill()
skyscrapers()
end_fill()


#        -------Doing the windows of the buildings----------


#Function Definition windows
def windows(between_win, lenght_win):
    fillcolor("#FFFFD4")
    left(90)
    penup()
    forward(9)
    pendown()
    right(90)

    for counter in range(4):
        penup()
        forward(between_win)
        pendown()
        begin_fill()
        left(90)
        forward(10)
        left(90)
        forward(lenght_win)
        left(90)
        forward(10)
        left(90)
        forward(lenght_win)
            
    left(90)
    penup()
    forward(29)
    pendown()

    for counter in range(4):
        begin_fill()
        left(90)
        forward(lenght_win)
        left(90)
        forward(10)
        left(90)
        forward(lenght_win)
        left(90)
        forward(10)
        left(90)
        penup()
        forward(between_win)
        pendown()
        right(90)
        end_fill()
    right(90)

#Collocating windows
#First building
setpos(-650, -100)
for counter in range (5):
    between_win = 18
    lenght_win = 10
    windows(between_win, lenght_win)
penup()
setpos(-560,-100)
pendown()

#Second building
for counter in range (6):
    between_win = 18
    lenght_win = 10
    windows(between_win, lenght_win)
penup()
setpos(-460,-100)
pendown()
#Third building
for counter in range (10):
    between_win = 23
    lenght_win = 15
    windows(between_win, lenght_win)
penup()
setpos(-340,-100)
pendown()
#Fourth building
for counter in range (12):
    between_win = 23
    lenght_win = 15
    windows(between_win, lenght_win)

penup()
setpos(-235,-100)
pendown()

#Fifth building
for counter in range (5):
    between_win = 19
    lenght_win= 7
    windows(between_win, lenght_win)
penup()
left(90)
forward(10)
right(90)
forward(45)
pendown()
begin_fill()
circle(7)
end_fill()
penup()
setpos(-140,-100)
pendown()

#Sixth building
for counter in range (4):
    between_win = 19
    lenght_win= 12
    windows(between_win, lenght_win)
penup()
backward(3)
left(90)
forward(8)
right(90)
forward(7)
pendown()
begin_fill()
forward(75)
left(90)
forward(40)
left(120)
forward(80)
left(150)
end_fill()
penup()
setpos(28,-100)
pendown()

#Seventh building
for counter in range (5):
    between_win = 19
    lenght_win= 7
    windows(between_win, lenght_win)
penup()
left(90)
forward(10)
right(90)
forward(45)
pendown()
begin_fill()
circle(7)
end_fill()
penup()
setpos(138,-100)
pendown()

#Eighth building
for counter in range (8):
    between_win = 21
    lenght_win= 15
    windows(between_win, lenght_win)
penup()
left(90)
forward(15)
right(90)
forward(20)
pendown()
begin_fill()
forward(50)
left(90)
forward(25)
left(90)
forward(12)
right(90)
circle(13,180)
right(90)
forward(12)
left(90)
forward(28)
left(90)
end_fill()
penup()
setpos(248,-100)
pendown()

#Nineth building
for counter in range (10):
    between_win = 23
    lenght_win = 15
    windows(between_win, lenght_win)
penup()
setpos(382,-100)
pendown()

#tenth building
for counter in range (8):
    between_win = 19
    lenght_win = 8
    windows(between_win, lenght_win)
penup()    
left(90)
forward(15)
right(90)
forward(36)
pendown()
begin_fill()
forward(28)
left(90)
forward(38)
left(60)
forward(22)
left(60)
forward(22)
left(60)
forward(38)
left(90)
end_fill()
penup()
setpos(482,-100)
pendown()

#Eleventh Building
for counter in range (4):
    between_win = 19
    lenght_win= 12
    windows(between_win, lenght_win)
penup()
backward(3)
left(90)
forward(8)
right(90)
forward(7)
pendown()
begin_fill()
forward(75)
left(90)
forward(40)
left(120)
forward(80)
left(150)
end_fill()
penup()
setpos(570,-100)
pendown()

#Twelveth building
for counter in range (10):
    between_win = 23
    lenght_win = 15
    windows(between_win, lenght_win)



#             -------Final detailas and decoration--------

    
#Filling sides of the road
for counter in range (1):
    fillcolor("#1F1111")
    penup()
    setpos(-650,-100)
    pendown()
    begin_fill()
    forward(580)
    right(120)
    pensize(4)
    forward(300)
    pensize(1)
    right(60)
    forward(560)
    right(90)
    forward(260)
    left(90)
    penup()
    setpos(650,-100)
    pendown()
    forward(620)
    left(120)
    pensize(4)
    forward(300)
    pensize(1)
    left(60)
    forward(560)
    left(90)
    forward(260)
    end_fill()

#Doing a moon
fillcolor ("#FFFF99")
penup()
setpos(-40,300)
pendown()
begin_fill()
left(22)
circle(50,270)
penup()
circle(50,90)
pendown()
end_fill()
fillcolor ("#160D50")
begin_fill()
left(35)
circle(38,200)
pencolor("#160D50")
circle(38,160)
end_fill()

#Doing some stars
penup()
pensize(3)
pencolor("#FFFF99")
setpos(-600,300)
dot("#FFFF99")
setpos(-630,295)
dot("#FFFF99")
setpos(-575,246)
dot("#FFFF99")
setpos(-478,268)
dot("#FFFF99")
setpos(-640,378)
dot("#FFFF99")
setpos(-350,320)
dot("#FFFF99")
setpos(-212,400)
dot("#FFFF99")
setpos(-150,320)
dot("#FFFF99")
setpos(-70,266)
dot("#FFFF99")
setpos(0,320)
dot("#FFFF99")
setpos(25,249)
dot("#FFFF99")
setpos(130,356)
dot("#FFFF99")
setpos(138,338)
dot("#FFFF99")
setpos(220,275)
dot("#FFFF99")
setpos(640,325)
dot("#FFFF99")
setpos(310,340)
dot("#FFFF99")
setpos(359,300)
dot("#FFFF99")
setpos(428,300)
dot("#FFFF99")
setpos(467,234)
dot("#FFFF99")
setpos(519,250)
dot("#FFFF99")





# End Turtle Library   
done()
# END





















