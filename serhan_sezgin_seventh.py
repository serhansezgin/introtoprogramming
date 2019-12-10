
'''
names1 = ['Amir', 'Bala', 'Chales']
if 'amir' in names1:
    print(1)
else:
    print(2)
'''


'''
myList = [1,5,5,5,5,1]
max = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > max:
        max = myList[i]
        indexOfMax = i
print(indexOfMax)
'''



'''
ffile = open("foot.txt")
 
shoes = []
 
for foot in ffile:
    try:
        f = float(foot)
        shoe = round(3/2.0 *(f + 1.5))
        print("Foot length:", f, "Suitable shoe size is", shoe)
        shoes.append(shoe)
    except:
        print("Invalid input")
 
while True:
    try:
        size = int(input("Please enter the size: "))
        number = shoes.count(size)
        print(number, "people have the same shoe size")
        break
    except:
        print("Please enter a number")
'''


'''
def day_of_week(n):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[n-1]
 
while True:
    line = input("Enter number of day of the week or word 'done': ")
    if line == 'done':
        break
    try:
        number = int(line)
        if number < 1 or number > 7:
            print("The number of day of the week must be in the range 1-7")
        else:
            print("The name of this day of the week is", day_of_week(number))
    except:
        print("Please enter a number")
'''


'''
celsius = [32, 10, 15.6, 24, 5.8]


for temp in celsius:
    print("Celcius",temp,"Fahrenheit:",temp*1.8+32)
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
filehandler = open("data2.txt")
for line in filehandler:
    line = line.rstrip()
    if line.endswith('.'):
        continue
    print(line)        
'''

'''
#Exercise1
ffile = open("temps.txt")
 
Fahrenheits = []
 
for celsius in ffile:
    try:
        c = float(celsius)
        fahrenheit = round(c*1.8+32)
        print("Celcius", c, "Fahrenheit", fahrenheit)
        Fahrenheits.append(fahrenheit)

    
    except:
        print("Invalid input")

print(max(Fahrenheits))
print(min(Fahrenheits))
print(sum(Fahrenheits)/len(Fahrenheits))
'''




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
'''
#Exercise2

def day_of_month(n):
    days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
    return days[n-1]


#print(day_of_month(2))


#while True:
filehandler = open("days.txt")
for line in filehandler:
    line = line.split('.')
    #print(line[1])  
    a= int(line[0])
    print(a,".month have", day_of_month(a), "days")
'''


def day_of_month(n):
    days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
    return days[n-1]
 
print(n,".month have", day_of_month(1), "days")






'''
x = "10@11@2019"
line = str(x.split('@'))
print(line)
'''




'''      
    try:
        number = int(line)
        if number < 1 or number > 7:
            print("The number of day of the week must be in the range 1-7")
        else:
            print("The name of this day of the week is", day_of_week(number))
    except:
        print("Please enter a number")
'''



#during session

'''
a = [2, 3, 1, 5]
b = [6, 4]
c = (a + b)

print (c)
print(sorted(c))
'''


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



def day_of_month(n):
    days = ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
    return days[n-1]



def month_as_name(month):
    names =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
'''


