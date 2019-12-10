'''
x = input('enter a number: ')
print(x)
'''


'''
x = int(input('enter a number: '))
print(x) 
'''

'''
our_list = [] # create empty list
 
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

our_list.append(first_num)
our_list.append(second_num)
our_list.append(third_num)


print(our_list)
'''

'''
our_list = [] # create empty list
 
for i in range(0, 5): # set up loop to run 5 times
	number = int(input('Please enter a number: ')) # prompt user for number
	our_list.append(number) # append to our_list



print(our_list)
'''

'''
n=int(input())
my_li=list(map(int,input().split()))
print(my_li)
'''

'''
mod_sum = [1,2,3,4,5]
for s in mod_sum:
    if 
'''


'''
#usedGameboardPosition = [[0 for x in range(16)] for x in range(16)]
usedGameboardPosition = [0,0,0,0]
#for x in usedGameboardPosition:

if all(x == 0 for x in usedGameboardPosition):
        #all(v == 0 for v in values)


        print(usedGameboardPosition)
        print ("All zeroes!")
'''


'''
#x = [[0 for x in range(16)] for x in range(16)]
x = [0,0,0,0,0]
print(x)
print (all(all(y == 0 for y in x) ))
'''





'''
try:
    if 2<=p<100:


except:
    break        
'''







# A school method based Python3 program  
# to check if a number is prime 
  
# function check whether a number  
# is prime or not 

n = int(input("please enter a number: "))

def isPrime(n): 
    while True:
        
    # Corner case 
                if (n <= 1): 
                    return False
  
    # Check from 2 to n-1 
                for i in range(2, n): 
                    if (n % i == 0): 
                        return False
  
                return True
  
# Driver Program  
if isPrime(n): 
        print ("true") 
else: 
        print ("false") 
      
# This code is contributed by Sachin Bisht 



