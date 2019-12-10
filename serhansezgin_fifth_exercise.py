'''
phrase = 'Fortune favors the bold'
print(phrase[20:])
'''

'''
print("Hello".replace("l", "e"))
'''


'''
phrase = "No man is an island"
for a in phrase:
    print(a)
'''
'''
#GYYMMDDSSSC

code = input("Please enter a personal identification number: ")
#example code: 48007140350

date = code[5] + code[6]
month = code[3] + code[4]

if code[0] == "1" or code[0] == "2":
    century = "18"
elif code[0] == "3" or code[0] == "4":
    century = "19"
else:
    century = "20"
 
year = century + code[1] + code[2]
 
print("The birthday of the person with the code", code, "is", date+"."+month+"."+year)
'''

'''
address = input("Please enter an address: ")
 
fpos = address.find("-")
lpos = address.find(",",fpos)
 
room = address[fpos+1:lpos]
 
print("Room number is", room)
'''



#Exercise 1. Name and grades
'''
fname = input('Please enter first name: ')
grades = input('Please enter grades: ')
count=0
for letter in grades.upper():
    if letter == 'A':
        count = count +1
    elif letter == 'B':
        count = count+1
print ("Hello", fname.capitalize() + ", your grades are",  grades.upper())
#print (fname.capitalize())
#print (grades.upper())
print("You have", len(grades),"grades")
print("Your grade for the second course is", grades[1].upper())
print("The number of A's and B's is", str(count))
'''

#Exercise 2. Username from url

'''
url = input('Please enter url: ')

tilda = url.find("~")
slash = url.find("/",tilda)

username = url[tilda+1:slash]

print("Username is", username)
'''

'''
During session 5
Exercises
1. Word Square
'''

'''
word = input('Please enter a word: ')

#for i in range (len(word)):
#a = word.upper()
#print(a)
#print((a+'\n')*len(word))
print((word.upper()+'\n')*len(word))
'''


'''
#solution
word = input('Please enter a word: ')

for letter in word:
    print(word.upper())


print("---------------------------")
i = 0
while i < len(word):
    print(word.upper())
    i += 1
print("---------------------------")

print((word.upper()+'\n')*len(word))

print("---------------------------")

for i in range(len(word)):
    print(word.upper())
'''



#2. Gender from an Estonian Personal Identifications Number



'''
#GYYMMDDSSSC

code = input("Please enter a personal identification number: ")
#example code: 48007140350



if code[0] == "1" or code[0] == "3" or code[0] == "5":
    gender = "Male"
elif code[0] == "2" or code[0] == "4" or code == "6":
    gender = "Female"

else:
    gender = "We havent come this century yet."
 

 
print("The gender of the person with the code", code, "is", gender)
'''

'''
#solution

code = input("Input ID: ")
g = int(code[0])

if g % 2 == 0:
    print("female")
else:
    print("male")
'''




'''
#3. Business card

fname =  input('Please enter your first name: ')
lname =  input('Please enter your last name: ')
mail =  input('Please enter your e-mail: ')
occu = input('Please enter your occupation: ')

print ("-"*40)
print( (("|"+'\n')*5))
print(((fname + " " + lname) + "- " + mail).center(40))
print(occu.center(40))
print ("-"*40)
#print(("|"+'\n')*5)
'''


'''
#solution

first =  input('Please enter your first name: ')
last =  input('Please enter your last name: ')
email =  input('Please enter your e-mail: ')
occupation = input('Please enter your occupation: ')

line = first + " " + last + " - " + email

width = len(line) + 20

print("+" + "-"*width + "+")

print("|" + "-"*width + "|")

print("|" + line.center(width) + "|")



print("|" + occupation.center(width) + "|")

print("|" + "-"*width + "|")

print("+" + "-"*width + "+")

'''







