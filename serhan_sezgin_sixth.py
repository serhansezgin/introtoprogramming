'''
filehandler = open("data.txt")
for line in filehandler:
    if "programming" in line:
        print(line)
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
username = "Mo\nty"
password = "Py\thon"
print("Username is " + username)
print("Password is " + password)
'''

'''
filehandler = open("data3.txt")
sum = 0
for line in filehandler:
    sum = sum + line
print(line)
'''

'''
filehandler = open("data4.txt")
a=0
for line in filehandler:
    a = a + len(line.rstrip())
print(a)
'''



'''
def shoe_size(length):
    return 1.5 * (length + 1.5)
 
ffile = open("foot.txt")
 
for foot in ffile:
    try:
        f = float(foot)
        s = shoe_size(f)
        print("Foot length:", f, "Suitable shoe size is", round(s))
    except:
        print("Invalid input")
 
ffile.close()
'''


'''
fname = input("Please enter the file name: ")
 
try:
    ffile = open(fname)
except:
    print("File cannot be opened:", fname)
else:
    for line in ffile:
        print(line.strip().upper())
    ffile.close()
'''



#Exercise 1


'''
url = input('Please enter url: ')

tilda = url.find("~")
slash = url.find("/",tilda)

username = url[tilda+1:slash]

print("Username is", username)
'''

'''
def find_name():
    print("Username is", username)
'''

'''
def find_name():

    url = open("urls.txt")
    for line in url:
        line = line.rstrip()
        #print(line)


        tilda = line.find("~")
        slash = line.find("/",tilda)

        username = line[tilda+1:slash]
    return username
    
find_name()
'''




#Exercise 2
'''
fname = input("Please enter the file name: ")
 
try:
    ffile = open(fname)
except:
    print("File cannot be opened:", fname)
else:
    count = 0
    for line in ffile:
        count += 1     
        print(str(count) + ".", line.strip())
            
    ffile.close()
'''


#Exercises during class
#1.Filtering Names
'''
fname = input("Please enter your last name: ")
 
try:
    ffile = open("names.txt")
except:
    print("File cannot be opened:", fname)
else:
    count = 1
    for line in ffile:
        if fname in line:
            print(str(count) + ".", line.strip())
            count += 1       
    ffile.close()
'''



#2. Odd or even
'''
numbersfile = open("oddeven.txt")
for line in numbersfile:
    if int(line)%2 == 0:
        print (line.strip(),"even")
    else:
        print (line.strip(),"odd")
'''

#3. Summing
'''
numbersfile = open("oddeven.txt")
sum_even = 0
sum_odd = 0
for line in numbersfile:
    if int(line)%2 == 0:
        
        print (line.strip(),"even")
        sum_even = sum_even + int(line)

    else:
        
        print (line.strip(),"odd")
        sum_odd = sum_odd + int(line)
print("sum even", sum_even)        
print("sum odd", sum_odd)
print("sum odd+even ", sum_odd+sum_even)
'''



#4. Horizontal bars
'''
file = open("numbers4hor.txt")
for line in file:
    print ("*"*int(line))
'''


#5. Upgraded budget

'''

'''


fname = input("Please enter the file name: ")
 
try:
    ffile = open(fname)
except:
    print("File cannot be opened:", fname)
else:
    inv_people = 0
    accepted_people = 0
    for line in ffile:
        if "?" in line:
            inv_people = inv_people + (line) 
            print(line.strip())

        if "+" in line:
            att_people = att_people + (line)
            print(line.strip())    
    ffile.close()


def budget(a):
    return ((10*a)+55)

#inv_people = int(input("Please enter the number of invited people: "))
#att_people = int(input("Please enter the number of people attending: "))

min_budget = budget(att_people)
max_budget = budget(inv_people)

print ("Min Budget",str(min_budget),"Euro")
print ("Max Budget",str(max_budget),"Euro")