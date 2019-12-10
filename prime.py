'''
num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           #print(num,"is not a prime number")  
           #print(i,"times",num//i,"is",num)  
           break  
   else:
'''


'''
p =int(input())

 # check for factors
for i in range(2,p):
        if (p % i) == 0 and p > 2:
            print(p,"is not a prime number")
            print(i,"times",p//i,"is",p)
            break
        else:
            print(p,"is prime number")
else:
    print(p,"is not prime")            
'''





'''
def isPrime(n): 
      
    # Corner case 
    if (n <= 1): 
        return False
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if (n % i == 0): 
            return False
  
    return True
  
# Driver Program  
if isPrime(11): 
    print ("true") 
else: 
    print ("false") 
'''




n = int(input("number: "))

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  
  
# Driver Program  
if (isPrime(n)) : 
    print(" true") 
else : 
    print(" false") 
'''      
if(isPrime(15)) : 
    print(" true") 
else :  
    print(" false") 
'''

