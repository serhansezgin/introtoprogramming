'''
def add(a, b):
    c = a + b
x = 3
y = 4
c = add(x, y)
return (c)
    add(3,4)
'''

s = 0
for i in [2,-4,-5,1,3]:
    if i > 0 :
        s += i
    else:
        s -= i
print(s)