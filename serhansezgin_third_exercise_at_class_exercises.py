'''
def addtwo(a,b):
    print(a+b)
    return(a+b)

print (addtwo(1,2) + 3)
'''

'''
def season(month):
    if month == 1 or month == 2 or month == 12:

        print("winter")

    elif month == 3 or month == 4 or month == 5:

        print("spring")

    elif month > 5 and month < 9:

        print("summer")

    else:

        print("autumn")

season(9)
'''


'''
def multiply(a,b):
    return a - b

print(multiply(5, 6))
print(multiply(1, 1))
print(multiply(10, 0))
'''


'''
print(max("Introdction") + max("to") + max("progamming"))
'''


'''
def shoe_size(length):
    size = 1.5 * (length + 1.5)
    return size

name = input("Enter your name: ")
foot = float(input("Enter your foot length (cm): "))
shoe = shoe_size(foot)

print("Dear " + name + ", your suitable shoe size is " +str(round(shoe)))

print("Shrek's shoe size is", round(shoe_size(foot)))
'''


'''
def maximum(a,b):
    if a < b:
        return b
    else:
        return a


try:
    x1 = int(input("Enter the first number: "))
    y1 = int(input("Enter the second number: "))
    m1 = maximum(x1,y1)

    print("The input numbers are", str(x1), "and", str(y1) + ". The greatest number is", str(m1) + ".")

    x2 = int(input("Enter the third number: "))
    y2 = int(input("Enter the fourth number: "))
    m2 = maximum(x2, y2)
    print("The input numbers are", str(x2), "and", str(y2) + ". The greatest number is", str(m2) + ".")
    if m2 > m1:
        print("The first greatest number is smaller.")
    else:
        print("The second greatest number is smaller.")
except:
    print("Please enter a number.")
 
#print("The input numbers are 2 and 5. The greatest number is", str(maximum(2,5)) + ".")
#print("The input numbers are 4 and 1. The greatest number is", str(maximum(4,1)) + ".")
'''




#Exercise 1
# Number of days in month with function



'''
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

    


'''
#sample
a = input("Please and the number of the month: ")

def number_of_days(a):
    if a == 1:
        return "January 30 days"
    else:
        return "February 28 days"
print (number_of_days(a))        
'''




#Exercise 2
#Price Difference

'''
def price_difference(a,b,c):
    return (b*c)-a

a = int (input("What is the price of the product? "))
b = int (input("What is the monthly payment on the first installment plan? "))
c = int (input("How many months does the first installment plan last? "))

x = price_difference(a,b,c)


b = int (input("What is the monthly payment on the second installment plan? "))
c = int (input("How many months does the second installment plan last?  "))

y = price_difference(a,b,c)



def analyzer(x,y):
    if x<y: 
        return "The first installment plan is better!, Because the price difference is", x, "But in another case", y
    else:
        return "The second installment plan is better!, Because the price difference is", y,  "But in another case", x
print (analyzer(x,y))
'''


#During Session 3


'''
#Ex1 Money Change
def money_change(a):
    return float(a*1.14)

gbp = float(input("Please enter the GBP amount: "))
gbp2 = float(input("Please enter the second GBP amount: "))

print ("The first pound's conversion is",round(money_change(gbp)), "Euro")
print ("The second pound's conversion is",round(money_change(gbp2)), "Euro")
'''



'''
#Ex2 What is the name of the month?

try:
    month = int(input("Please enter the number of the month? "))

    def month_as_name(month):

        if month == 1:
            return("January")
    
        elif month == 2:
            return("February")
        elif month == 3:
            return("March")
        elif month == 4:
            return("April")
        elif month == 5:
            return("May")
        elif month == 6:
            return("June")
        elif month == 7:
            return("July")
        elif month == 8:
            return("August")
        elif month == 9:
            return("September")
        elif month == 10:
            return("October")
        elif month == 11:
            return("November")
        elif month == 12:
            return("December")    
        elif month == 0:
            return("The number of a month must be in the range [1-12]")

        else:
            return("There are only 12 months in a year.")                    
    
    print(month_as_name(month))

except:
    print("Please enter a valid number between [1-12]")
'''



#Ex3 Date as String

'''
try:

    day = int (input("Please enter the day: "))
    month = int(input("Please enter the number of the month? "))
    year = int(input("Please enter the year? "))
    

    def month_as_name(month):
    

        if month == 1:
            return("January")
    
        elif month == 2:
            return("February")
        elif month == 3:
            return("March")
        elif month == 4:
            return("April")
        elif month == 5:
            return("May")
        elif month == 6:
            return("June")
        elif month == 7:
            return("July")
        elif month == 8:
            return("August")
        elif month == 9:
            return("September")
        elif month == 10:
            return("October")
        elif month == 11:
            return("November")
        elif month == 12:
            return("December")    
        elif month == 0:
            return("The number of a month must be in the range [1-12]")

        else:
            return("There are only 12 months in a year.")                    
    man = (month_as_name(month))
    def whole_date(day,man,year):
        return (man,day,year)
    
    print (whole_date(day,man,year))

except:
    print("Please enter a valid number between [1-12]")

'''


'''
# 4 Budget

def budget(a):
    return ((10*a)+55)

inv_people = int(input("Please enter the number of invited people: "))
att_people = int(input("Please enter the number of people attending: "))

min_budget = budget(att_people)
max_budget = budget(inv_people)

print ("Min Budget",min_budget,"Euro")
print ("Max Budget",max_budget,"Euro")
'''

#5 Money
'''
def enough_money(price, amount, savings):
    total_price = price * amount
    if total_price < savings:
        return True
    else:
        return False
 
if enough_money(2, 4.5, 10):
    print('Buy')
else:
    print('Save more money')
'''

'''
def enough_money_trial(price,amount,savings):
    return (price*amount<savings)

if enough_money_trial(2, 4.5, 10):
    print('Buy')
else:
    print('Save more money')
'''



