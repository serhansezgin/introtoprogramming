from turtle import *
import turtle 

''' 
setup(600, 400)
title("Flag of Japan")
speed(10)
 
penup()
right(90)
forward(100)
left(90)
pendown()
 
color("red")
begin_fill()
circle(100)
end_fill()
 
exitonclick()
'''


'''
for i in range(4):
    forward(250)
    left(90)
    forward(150)
    left(90)
    color("red")
    begin_fill()
    #shape("rectangle") 
    end_fill()


    penup()
    left(90)
    forward(250)     # this moves the pen, but no line is drawn
    pendown()
    forward(250)
    left(90)
    forward(150)
    left(90)
    color("red")
    begin_fill()
    shape("rectangle")
    end_fill()

exitonclick()
'''



'''
for clr in ["yellow", "red", "purple", "blue"]:
    color(clr)
    forward(250)
    left(90)
exitonclick()
'''


'''
setup(600, 400)
title("Flag of Japan")
speed(10)
 
penup()
right(90)
forward(100)
left(90)
pendown()
 
color("red")
begin_fill()
circle(100)
end_fill()
 
exitonclick()
'''


setup(600, 600)
bgcolor("lightblue")
speed(10)

for i in range(4):
    forward(250)
    left(90)
    forward(100)
    left(90)
    color("blue")
    begin_fill()
    fillcolor("blue")
    end_fill()
penup()
right(90)
forward(100)
left(90)
pendown()
for i in range(4):
    forward(250)
    left(90)
    forward(100)
    left(90)
    color("black")
    begin_fill()
    fillcolor("red")
    end_fill()
penup()
right(90)
forward(100)
left(90)
pendown() 
for i in range(4):
    forward(250)
    left(90)
    forward(100)
    left(90)
    color("white")
    begin_fill()
    fillcolor('#FFA500')
    end_fill()

 
exitonclick()