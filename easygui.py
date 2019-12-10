'''
from easygui import * # in order to use EasyGui, you must import it.
 
buttons = ["easy","ok","difficult"]
pressed = buttonbox("Programming is ", choices = buttons) 
msgbox("My first graphical user interface!!") # message box




from easygui import *
 
mychoices = ["my favorite","easy","ok","difficult"]
pressed = choicebox("Programming is ", choices = mychoices)
if pressed == None:
    msgbox("You did not choose anything, you little rebel!")
elif pressed == "my favorite":
    msgbox("Programming is your favorite course! As it should be!")
else:
    msgbox("So you think that programming is " + pressed + ", hmm, interesting!")
'''

from turtle import *
right(60)
forward(100)
left(120)
forward(100)
exitonclick()







