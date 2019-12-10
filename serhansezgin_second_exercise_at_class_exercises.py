
#example 1
"""
age_as_string = input("How old are you? ")
try:
    age = int(age_as_string)
except:
    age = -1
 
if age < 1:
    print("This is not a valid age")
elif age < 18:
    print("In Estonia, you are considered as a minor")
elif age < 100:
    print("You are an adult")
else:
    print("Wow, you need a lot of birthday candles!")
"""


#example 2

"""
try:
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    if x == y:
        print('Numbers are equal')
    else:
        if x < y:
            print(x, 'is less than', y)
        else:
            print(x, 'is greater than', y)
except:
    print('Please enter a number')
"""




#exercise 1 Admission to UT.

"""
score_as_string = input("Please enter your admission score? ")
try:
    score = int(score_as_string)
except:
    score = -1
 
if score < 1:
    print("Enter a number of points", score)
    print("You cannot obtain negative points")
elif score < 66:
    print("Enter a number of points:", score)
    print("The obtained points are not enough to be considered for admission")
elif score > 100:
    print("Enter a number of points:", score)
    print("You cannot obtain so many points")
elif score >= 66:
    print("Enter the number of points:", score)
    print("The obtained points are enough to be considered for admission")
else:
    print("You must write a correct score as a number")
"""



#Exercise 2. Number of days in months

"""
try:
    x = int(input('Enter the number of the month: '))
    
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
        print('That month has 31 days in it')
    elif x==2:
        print("That month has 28 days in it")
    
    elif x==4 or x==6 or x==9 or x==11:
        print("That month has 30 days in it")
    
    else:
        if x<1 or x>12:
            print("The number of a month must be in the range [1-12]")
        
except:
    print('Please enter a number')
"""


#Optional Part

"""
try:
    x = int(input('Enter the number of the month: '))
    
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
        print('That month has 31 days in it')
    elif x==2:
        year = int(input("Enter a year:"))
        if year%4 != 0:
            print("hat month has 28 days in it (a common year).")
        elif year%4 == 0 and year%100 !=0:
            print("That month has 29 days in it (a leap year).")     
        elif year%100 == 0 and year%4 == 0: 
                 if year%400 == 0:
                    print("That month has 29 days in it (a leap year).") 
                 else:
                    print("That month has 28 days in it (a common year).")
    
    elif x==4 or x==6 or x==9 or x==11:
        print("That month has 30 days in it")
    
    else:
        if x<1 or x>12:
            print("The number of a month must be in the range [1-12]")
        
except:
    print('Please enter a number')

"""   




#during session 2


"""
try:
    score = int(input("Please enter your score? "))

 
    if score <= 50 and score >= 0:
        print("F")
    elif score > 50 and score <= 100 and score >= 0:
        ask = input("Enter course type(differentieated (d) / non-differentiated(n)):")
        if ask == "n":
            print("Pass")
        elif ask == "d":
            if score >=91:
                print("A")
            elif score >=81:
                print("B")
            elif score >=71:
                print("C")
            elif score >=61:
                print("D")
            elif score >=51:
                print("E")
            elif score <51:
                print("F")
        else:
            print("Your score must be between [0-100]")                    
    else:
        print("Score must be in the range [0-100].")

except:
    print("Please enter a valid number between [0-100]")

"""




#2. What is the name of the month?


"""
try:
    month = int(input("Please enter the number of the month? "))

 
    if month == 1:
        print("January")
    
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")    
    elif month == 0:
        print("The number of a month must be in the range [1-12]")

    else:
        print("There are only 12 months in a year.")                    
    

except:
    print("Please enter a valid number between [1-12]")
"""



#3. Number of days in month

#i did it already in the homework before - Optional Part

"""
try:
    x = int(input('Enter the number of the month: '))
    
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
        print('That month has 31 days in it')
    elif x==2:
        year = int(input("Enter a year:"))
        if year%4 != 0:
            print("hat month has 28 days in it (a common year).")
        elif year%4 == 0 and year%100 !=0:
            print("That month has 29 days in it (a leap year).")     
        elif year%100 == 0 and year%4 == 0: 
                 if year%400 == 0:
                    print("That month has 29 days in it (a leap year).") 
                 else:
                    print("That month has 28 days in it (a common year).")
    
    elif x==4 or x==6 or x==9 or x==11:
        print("That month has 30 days in it")
    
    else:
        if x<1 or x>12:
            print("The number of a month must be in the range [1-12]")
        
except:
    print('Please enter a number')

"""   



#4*. Students



students = int(input("Please enter students numbers:"))
rooms = int(input("Please enter rooms numbers "))

s_div_r = students//rooms

#print(s_div_r)
s_remainder_r = students%rooms
#print(s_remainder_r)

second_cacl = s_remainder_r % s_div_r
#print(second_cacl)
#print("At the beginning",  int(second_cacl+s_div_r) , "students can be arranged by per" ,int(s_remainder_r) , "rooms")
print("In", int(s_remainder_r), "classes there are", int(second_cacl+s_div_r), "students") 
number_of_other_rooms = rooms - s_remainder_r

#print(number_of_other_rooms)


last_calc = s_remainder_r//number_of_other_rooms
#print(last_calc)
#print("the remainins", last_calc, "students can be arranged by per", number_of_other_rooms, "rooms"  )
print("In", number_of_other_rooms, "classes there are", last_calc, "students") 


