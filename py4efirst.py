
#breaking put of a loop
"""
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')
"""
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
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')
'''



#a definite loop with strings

'''
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print("Done!")
'''



#what is the largest number
#3,41,12,9,74,15

#mine
'''
numbers = [3,41,12,9,74,15]
for number in numbers :
    max = numbers[0]

    for (i=0;i<=numbers.length) :
    if (numbers[i]>numbers[0]) :
        max = numbers[i]
        print(max)
'''


#https://www.youtube.com/watch?v=8DvywoWv6fI
#Python for Everybody - Full Course with Dr. Chuck
#what is the largest number
'''
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [3,41,12,9,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)
'''


#counting in a lopp
'''
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)    
'''


#summing in a loop
'''
zork = 0
print('Before', zork)
for thing in (9,41,12,3,74,15) :
    zork = zork + thing
    print('before', thing, 'add', zork)
print('After', zork)
'''



#finding the average in a loop
'''
count = 0
sum = 0
print('Before', 'count', count, 'sum', sum)
for value in [9,41,12,3,74,15] :
    count = count + 1
    sum = sum + value
    print('count', count, 'new add', value, 'result', sum)
print('After', 'count', count, 'sum', sum, 'Average', sum / count)
'''


#filtering in a loop
'''
print('Before')
for value in [9,41,12,3,74,15] :
    if value > 20 :
        print('Large Number',value)
print('After')
'''



#search using a boolean variable

'''
found = False
print('Before', found)
for value in [9,41,12,3,74,15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)
'''


#how to find the smallest value
'''
smallest_so_far = 10
print('Before', smallest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print('After', smallest_so_far)
'''

#finding the smallest value
#teacher
'''
smallest = None
print('Before')

for value in [9,41,12,3,74,15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)
'''



#is is-not operators

#is is more powerful than ==




#strings
'''
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)


str3 = '123'
#str3 = str3 + 1

x = int(str3) + 1
print(x)
'''

#reading and converting

'''
name = input('Enter something: ')
print(name)
'''

'''
apple = input('Enter:')
#x = apple + 'banana'
x = int(apple) - 10
print(x)
'''



'''
fruit = 'banana'
#letter = fruit[1]
#print(letter)



x=3
w=fruit[x-1]
print(w)
'''

'''
#len function

fruit = 'banana'
x = len(fruit)
print(x)
'''


#looping through strings

'''
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
'''

'''
fruit = 'banana'
for letter in fruit:
    print(letter)
'''


#looping and counting
'''
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)
'''
'''
word = 'bananaaaaaaaaaaaaaaaaaasssssssseeeeeeeeeaaaaaaaaaaaa'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)
'''


'''
#looking deeper into in
for letter in 'banana' :
    print(letter)
'''


'''
#slicing strings

#Monty Pyth o n
#01234567891011

s = 'Monty Python'
print(s[0:4])

print(s[6:7])

print(s[6:20])




print (s[:2])

print (s[8:])

print (s[:])

'''


'''
fruit = 'banana2'
print('n' in fruit)

'm' in fruit

'nan' in fruit


if 'a' in fruit :
    print('Found it!')
'''

'''
word = 'banana'
if word == 'banana':
    print('All right, bananas.')


if word < 'banana':
    printf('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    printf('Your word,' + word + ', comes before banana.')
else:
    print("All right, bananas.")    
'''


'''
#string library

greet = 'Hello Boy'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())
'''
'''
fruit = 'banana2'
print('n' in fruit)
'''

'''
stuff = 'Hello world'
print(type(stuff))
print(dir(stuff))
'''


#string library


#x = str.capitalize('ananas')
#print(x)

#print(str.center('           ananas'))


#print(str.strip(['ananas'])


#print(str.upper('ananas'))


'''
fruit = 'banana'
pos = fruit.find('na')
print(pos)


aa = fruit.find('z')
print(aa)
'''

'''
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)


www = greet.lower()
print(www)
'''


'''
greet = 'Hello Bob'
#nstr = greet.replace('Bob','Jane')
#print(nstr)
'''

'''
nstr = greet.replace('o','X')
print(nstr)
'''

'''
greet = 'Hello Bob Bob Greta Zeppelin Bob'
nstr = greet.replace('Bob','')
print(nstr.strip())
'''

'''
#stripping whitespace

greet = '  Hello Bob     '
print(greet.lstrip())

print(greet.rstrip())
print(greet.strip())
'''




'''
line = 'Please have a nice day'
print(line.startswith('Please'))


print(line.startswith('p'))
'''



'''
#from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

data = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)


host = data[atpos+1 : sppos]
print(host)
'''

'''
fhand = open('mbox.txt')
print(fhand)
'''

'''
stuff = 'Hello\nWorld!'
print(stuff)


stuff = 'X\nY'
print(stuff)    

print(len(stuff))
'''
'''
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
'''

'''
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
'''

'''
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:38])
'''

'''
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line)
'''


'''
fhand = open('mbox-short.txt')
for chese in fhand:
    if chese.startswith('From:') :
        print(chese)
'''

#line or chese all works

#rstrip is for stripping the whitelines
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
'''
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)
'''



#using in to select lines
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line :
        continue
    print(line)
'''
'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if '@uct.ac.za' in line:

        print(line)
'''


'''
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)
'''




#for bad file names
'''
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)    
    quit()  #quit is important here, comes in and never returns
    #finsh the file silently, without giving traceback

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)
'''


'''
friends = ['Joseph', 'Giane', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')
'''
'''
z = ['Joseph', 'Giane', 'Sally']
for x in z:
    print('Happy New Year:', x)
print('Done!')
'''

'''
friends = ['Joseph', 'Giane', 'Sally']
print(friends[1])
'''


#list are mutable
#you cant assign a string another chars, 
# but you can use fruit.lower for example

'''
fruit = 'Banana'
#fruit[0] = 'b'



x = fruit.lower()
print(x)
'''

'''
lotto = [2,14,26,41,63]
print(lotto)
lotto[2] = 28
print(lotto)
'''



'''
greet = 'Hello Bob'
print(len(greet))


x = [1,2,'joe',99]
print(len(x))
'''


#using the range function
'''
print(range(4))

friends = ['joseho', 'Gienn', 'Sally']
print(len(friends))

print(range(len(friends)))
'''

#a tale of two loops
'''
friends = ['joseho', 'Gienn', 'Sally']

for friend in friends :
    print('Happy New Year:', friend)

for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Fucking Year:', friend)
'''


'''
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

print(a)
'''
'''
x = list()
print(type(x))

print(dir(x))
'''


'''
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)
'''

'''
some = [1,9,21,10,16]
print(9 in some)
print(15 in some)
print(20 not in some)
'''

'''
friends = ['Joseh', 'Glessn', 'Sally']
friends.sort()
print(friends)
print(friends[1])
'''


#built-in functions and lists
'''
nums = [3,41,12,9,74,15]
print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums))

print(sum(nums)/len(nums))
'''

'''
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)
'''


'''
numlist = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)


average = sum(numlist) / len(numlist)
print('Average:', average)
'''

'''
abc = 'With three words'
stuff = abc.split()
print(stuff)
#['With', 'three', 'words']

print(len(stuff))

print(stuff[0])


for w in stuff :
    print(w)
'''


'''
line = 'A lot              of spaces'
etc = line.split()
print(etc)
'''


'''
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))


thing = line.split(';')
print(thing)

print(len(thing))
'''


'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
'''



'''
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)
email = words[1]
print(email)


pieces = email.split('@')
print(pieces[1])
'''





'''
han = open('mbox-short_.txt')

for line in han:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    print(wds)
'''


'''
han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()    #throws out the whitespace
    
    wds = line.split()
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])
'''



'''
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)
'''



#comparing lists and dictionaries
#dictionaries are like lists except that they use keys instead of numbers to look up values
'''
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)
'''
'''
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)


ddd['age'] = 23
print(ddd)
'''


#many counters with a dictionary

'''
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)


ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
'''


#dictionary tracebacks
'''
ccc = dict()
#ccc['csev'] = 1
print(ccc['csev'])
'''


#when we see a new name
'''
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

#the get method for dictionaries
if name in counts:
    x = counts[name]
else :
    x = 0
x = counts.get(name, 0)
print(x)
'''
#simplified counting with get()
#we can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one
'''
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)
'''
#counting with words
#counting pattern
'''
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)
'''



'''
counts = dict()
line = input('Enter a line of text:')
words = line.split()

print('Words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)
'''


#define loops and dictionaries
'''
counts = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
for key in counts:
    print(key, counts[key])
'''


#retrieving lists of keys and values

'''
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan' : 100}
print(list(jjj))

print(jjj.keys())

print(jjj.values())

print(jjj.items())
'''

#bonus: two iteration variables!
'''
jjj = { 'chuck' : 1 , 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items() :
    print(aaa, bbb)
'''

'''
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1


bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
'''

'''

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        #if the key is not there, the count is zero
        #print('**',w,di.get(w,-99))

        #oldcount = di.get(w,0)

        #print(w,'old',oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        print(w,'new',di[w])


        #print('start of new word:')
        #print(w)
        if w in di :
            di[w] = di[w] + 1
            #print('**Existing**')
        else:
            di[w] = 1
            #print('**NEW**')    
        print(w, di[w])

print(di)

'''


'''
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        #print(w,'new',di[w])


#print(di)

#now we want to find the most common word
largest = -1
theword = None
for k,v in di.items() :
    #print(k,v)
    if v > largest :
        largest = v
        theword = k #capture/remember the word that was largest


print(theword, largest) 

'''



#tuples are like lists
'''
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = ( 1,9,2 )
print(y)

print(max(y))
'''




#but tuples are immutable
'''
x = [9,8,7]
x[2] = 6
print(x)
'''
'''
y = 'ABC'
y[2] = 'D'
'''
'''
z = (5,4,3)
z[2] = 0
'''



#things not to do in tuples
'''
x = (3,2,1)
x.sort()

x.append(5)

x.reverse()
'''

'''
l = list()

print(dir(l))
'''

'''
t = tuple()
print(dir(t))
'''



'''
(x,y) = (4, 'fred')

print(y)
'''

'''
(a,b) = (99,98)
print(a)
'''



#tuples and dictionaries
'''
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)




tups = d.items()
print(tups)
'''

'''
print ((0,1,2) < (5,1,2))

print ((0,1,200000) < (0,3,4))

print (    ('Jones', 'Sally')    <       ('Jones', 'Sam')          )

print (    ('Jones', 'Sally')    >       ('Adams', 'Sam')          )
'''


# sorting lists of tuples
'''
d = {'a':10, 'b':1, 'c':22}
print(d.items())


print(sorted(d.items()))


for k,v in sorted(d.items()):
    print(k,v)
'''

'''
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items() :
    tmp.append( (v, k) )
print(tmp)




tmp = sorted(tmp, reverse=True)
print(tmp)
'''

'''
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)
'''

'''
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))
'''

'''
fname = input ('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

#print(di)

tmp = list()
for k,v in di.items() :
    #print(k,v)
    newt = (v,k)
    tmp.append(newt)
#print('Flipped', tmp)

tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])


for v,k in tmp[:5] :
    print(k,v)
'''

'''
import re
#regular expressions

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
    #if line.find('From:') >= 0:
    #if line.startswith('From:') :
    #if re.search('^From:', line) :
        print(line)
'''
'''
import re
#regular expressions

hand = open('regularexp.txt')
for line in hand:
    line = line.rstrip()
    
    if re.search('^X.*:', line) :   #X plus one or more characters ending with semicolon
    #if re.search('^X-\S+:', line) :  #X plus non space characters one or more, ending with semicolon
        print(line)
'''

'''
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)   #  [0-9]+ one or more digits
print(y)
y = re.findall('[AEIOU]+',x)
print(y)
'''

'''
#greedy matching
import re
x = 'From: Using the : character'
y = re.findall('^F.*:', x)  #Greedy (longer) matching
print(y)
'''

'''
#non greedy matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)  #one or more character but not greedy
print(y)                     #prefers the shorter one
'''

'''
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan    5 09:14:16 2008'
#y = re.findall('\S+@\S+',x) #\S+@\S+ at least one non-whitespace character
y = re.findall('^From (\S+@\S+)',x) #paranthesis in reg do the extraction in paranthesis
print(y)
'''


'''
import re
data = 'From stephen.marquard@uct.ac.za Sat Jan    5 09:14:16 2008'
atpos = data.find('@')
print(atpos)


sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
'''



'''
#double split pattern
import re
line = 'From stephen.marquard@uct.ac.za Sat Jan    5 09:14:16 2008'

words = line.split()
print('words: ',words)
email = words[1]
print('email: ', email)
pieces = email.split('@')
print('pieces: ',pieces)
print('pieces[1]: ',pieces[1])
'''



'''
#the regex version
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan    5 09:14:16 2008'

y = re.findall('@([^ ]*)',lin)
print(y)
'''
'''
#even cooler regex version

import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan    5 09:14:16 2008'

y = re.findall('^From .*@([^ ]*)',lin)
print(y)
'''

'''
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
'''

'''
#Escape Character

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x) 
#backslash  if you want a special reg ex carachter to just behave
#normally (most of the time) you prefix it with '\'
print(y)
'''

'''
#networking
#sockets in python
#python has built-in support for TCP Sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
'''

'''
#An HTTP Request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4e.com/code3/romeo.txt', 443))
cmd = 'GET https://www.py4e.com/code3/romeo.txt\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
'''


#using urllib in Python
#since HTTP is so common, we have a library that does all the socket
#work for us and makes web pages look like a file

'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
'''

#like a file
#how to read and count from a webpage via python
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split() #decode becuase the lines are byte not string
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
'''


#reading web pages
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
'''


#parsing htmls

#scraping web sites

#the easy way - Beautiful Soup
#you could do the string searches the hardway
#or use the free software libary called Beautiful Soup from
# www.crummy.com

# via beautifulsoup
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
'''



'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
'''

'''
import xml.etree.ElementTree as ET

data = '''
#<person>
 #   <name>Chuck</name>
  #  <phone type="intl">
   #     +1 734 303 4456
    # </phone>
     #<email hide="yes"/>
#</person>'''

'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
'''


"""
import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
"""




#java script object notation
#json

"""
import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes"
            }
        }'''
    
info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])
"""


"""

import json
input = '''[
  {  "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    } ,
    { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
   ]'''
    
info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

"""


#using web services
#Service Oriented Approach

#08.04.12

'''
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter locations: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
'''


"""
#twitter2.py to retrieve an account's twitter friends



import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])
"""





#OOP
#Object Oriented Programming
#sqlite3 uses objects
'''
inp = input('Europe Floor?')
usf = int(inp) + 1
print('US Floor', usf)
'''

'''
class PartyAnimal:
    x=0


    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
'''

'''
y = 'Hello there'
print(dir(y))
'''

'''
class PartyAnimal:
    x=0

    def __init__(self):
        print('I am constructed')


    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)

    def __del__(self):
        print('I am desctructed', self.x)   

an = PartyAnimal()

an.party()
an.party()
an = 42
print('an contains',an)
'''

'''
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name,"constructed")


    def party(self) :
        self.x = self.x + 1
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
s.party()


j = PartyAnimal("Jim")
j.party()
s.party()
'''
'''
#inheritance

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name,"constructed")


    def party(self) :
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()


j = FootballFan("Jim")
j.party()
j.touchdown()

'''



#web appliacations w/ Databases


#SQL Summary

"""
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
DELETE FROM Users WHERE email='ted@umich.edu'
UPDATE Users SET name="Charles" WHERE email='csev@umich.edu'
SELECT * FROM Users
SELECT * FROM Users WHERE email='csev@umich.edu'
SELECT * FROM Users ORDER BY email
'''
'''
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
        VALUES (?, 1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()


#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

"""


"""
#twspider


from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

cur.close()

"""

"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

#Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    artist_id INTEGER,
    title TEXT UNIQUE
    );

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)
);
)

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'


"""


"""
print("hello me")

"""



















































































































































































