
#serhan sezgin
#before session 4 trials from videos

'''
n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')
print(n)
'''


'''
n=5
while n>0:
    print('Lather')
    print('Rinse')
print('Dry off!')
'''


'''
n=0
while n>0:
    print('Lather')
    print('Rinse')
print('Dry off!')
'''

'''
while True:
    line=input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')
'''


'''
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
'''

'''
while True:
    line = raw_input('> ')
    if line[0] == '#':
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
'''



#Definite Loops

'''
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
'''


'''
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
'''




#largest number

'''
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)
'''



#counting

'''
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork, thing)
print('After', zork)
'''



#summing in a loop
'''
zork =0
print('Before', zork)
for thing in [9,41,12,3,74,15] :
    zork = zork + thing
    print(zork,thing)
print('After', zork)
'''



#Finding the average in a loop
'''
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)
'''



#Filtering in a loop
'''
print('Before')
for value in [9,41,12,3,74,15] :
    if value > 20:
        print('Large number',value)
print('After')
'''


#search using a boolean variable
'''
found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)
'''



'''
s = 0
for i in [1,2,3,4,5,6,7]:
    s=s*i
print(i)    
'''


'''
while True:
    word = input("Say something: ")
    if word == "programming":
        continue
    if word == "bye":
        break
    print("Very interesting!")
'''


'''
i=0
while i<5:
    print("Hello!")
    i = i+1
    print(i)
'''

'''
def repeat(number,word):
    while number > 0:
        print(word)
repeat(4, "line")        
'''


'''
print("Finding sum with for loop")
sum1 = 0
for i in [1,2,3,4,5,6,7,8,9]:
    sum1 = sum1 + i
    print("Sum so far", sum1)
print("Sum of numbers 1-9 is", sum1)
 
print("Finding sum with while loop")
sum2 = 0
a = 1
while a < 10:
    sum2 = sum2 + a
    print("Sum so far", sum2)
    a += 1
print("Sum of numbers 1-9 is", sum2)
'''



'''
def maximum(a, b):
    if a < b:
        return b
    else:
        return a
 
while True:
    line = input("Enter the first number or word 'done': ")
    if line == 'done':
        break
    line2 = input("Enter the second number: ")
    try:
        x = int(line)
        y = int(line2)
        m = maximum(x, y)
        print("The maximum of numbers", x, "and", y, "is", m)
    except:
        print("Please enter a number")
''' 


'''
x = int (input("Please enter a number: "))
i=0
while i<9:
    
    i = i+1
    print(i*x)
'''


#exercise 2
#number of days

'''
while True:
    line = input("Enter the first number or word 'done': ")
    if line == 'done':
        break
try:
    x = int(input('Enter the number of the month: '))


    def number_of_days(x):

    
        if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
            return('That month has 31 days in it')
        elif x==2:
            year = int(input("Enter a year:"))
            if year%4 != 0:
                return("hat month has 28 days in it (a common year).")
            elif year%4 == 0 and year%100 !=0:
                return("That month has 29 days in it (a leap year).")     
            elif year%100 == 0 and year%4 == 0: 
                 if year%400 == 0:
                    return("That month has 29 days in it (a leap year).") 
                 else:
                    return("That month has 28 days in it (a common year).")
    
        elif x==4 or x==6 or x==9 or x==11:
            return("That month has 30 days in it")
    
        else:
            if x<1 or x>12:
                return("The number of a month must be in the range [1-12]")


    print(number_of_days(x))            
        
except:
    print('Please enter a number')
'''



#during session 4

'''
mantra = input("Enter your mantra: ")
number=int(input("How many times to repeat: "))
#print((mantra+'\n')*number)


i=0
while i < number:
    print(mantra)
    i+=1
'''
'''
for i in range(1,number+1):
    print(mantra*i)
'''






#2.Triangle
'''
number = int(input("How many times to repeat: "))

'''
"""
i=0
while i < number:
    print("*"*i)
    i+=1

'''
for i in range(1,number+1):
    print('*'*i)
"""


#3.integers that are not divisible by 10

'''
m = int(input("Please enter a number: "))
n = int(input("Please enter a second number: "))


if m<n:
    i=0
    for i in range(m,n):
        if i % 10 != 0:
            print(i)
    i=i+1
    
elif n<m:
    i=0
    for i in range(n,m):
        if i % 10 != 0:
            print(i)
    i=i+1
'''








#4.Celcius and Fahrenheit

'''
celsius = [32, 10, 15.6, 24, 5.8]


for temp in celsius:
    print("Celcius",temp,"Fahrenheit:",temp*1.8+32)
'''



#5. The three-year child simulator
'''
while True:
    line = input("Enter the first number or word 'done': ")
    if line == 'done':
        break
    line2 = input("Enter the second number: ")
    try:
        x = int(line)
        y = int(line2)
        m = maximum(x, y)
        print("The maximum of numbers", x, "and", y, "is", m)
    except:
        print("Please enter a number")
'''

'''
line = input("Which is the clouds consist of? ")
while True:
    ask = input("But why? ")
    if ask == 'magic':
        break
'''
'''
answer = input("Which is the clouds consist of? ")
while answer != 'magic':
    answer = input("But why?")
'''

#Exercises 2

'''
def number_of_days(x):

    
        if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
            return('That month has 31 days in it')
        elif x==2:
            year = int(input("Enter a year:"))
            if year%4 != 0:
                return("hat month has 28 days in it (a common year).")
            elif year%4 == 0 and year%100 !=0:
                return("That month has 29 days in it (a leap year).")     
            elif year%100 == 0 and year%4 == 0: 
                 if year%400 == 0:
                    return("That month has 29 days in it (a leap year).") 
                 else:
                    return("That month has 28 days in it (a common year).")
    
        elif x==4 or x==6 or x==9 or x==11:
            return("That month has 30 days in it")
    
        else:
            if x<1 or x>12:
                return("The number of a month must be in the range [1-12]")

while True:
    line = input("Enter the month or word 'done': ")
    if line == 'done':
        break


    try:
        x = int(line)
        print(number_of_days(x))            
        
    except:
        print('Please enter a months number')

'''






#/////////////////////////////////////////////////////////////////////////
#3. Integers that are not divisible by 10


'''
n = 5
while n>0:
    print(n)
    n=n-1
print('Blast!')
print(n)
'''

'''
for i in range (0,5):
    print(i)
'''

'''
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')
'''

'''
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
'''


'''
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
'''

'''
for i in range(0,5):
    i = i+1
    print(i)
'''



'''
print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print("After")    
'''


























