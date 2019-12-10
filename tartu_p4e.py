#print("tartu introduction to programming lecture 1")

"""
#1
name = input('Enter Your Name: ')
print('Hello '+ name)
print('Hello',name)
print("Hello" + str(2))
#print("Hello" + 2) number cant work in concatanation
"""

"""
#2
ects = input('Enter Your ECTS: ')
weeks = input("How many weeks you will take this course: ")


print ("Hours per week: ", ((26*int(ects))/int(weeks)))
"""


'''
#lecture
ects_string = input("Enter ECTS: ")
ects = int(ects_string)

weeks = int(input("Enter weeks: " ))

hours = ects*26/weeks

print("Hours per week -", hours)
'''




"""
#3
c = input("Please enter c: ")
f = (float(c) * float(9/5)) + float(32)
print (f)
"""

"""
#4
width = 17
height = 12.0
print (float (width/2))
print (float (width/2.0))
print (int (width/17))
print (int(width//2))
print (float(width//2.0))
print (int(width%2))
print (float(height/3))
print (int(1+2*5))
"""

'''
#5
name = input ("Enter your name: ")
footsize = (input("Enter your footsize in cm: "))
footlength = float(footsize)

shoesize = float(1.5) * (float(footlength) + float(1.5))

print ("Dear " + name + "your suitable shoe size is " , round(shoesize))
'''



