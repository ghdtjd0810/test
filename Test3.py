


#교수님답
'''
elst = [s[0]]
c = 1

for n in range(len(s)-1):
    if s[n] == s[n+1]:
        c+=1
    else:
    elst.append(c)
    elst.append(s[n+1])
    
elst.append(c)
print(elst)



number = 0
for i in range(1,11):
    number = number + i

print(number)

'''

def is_print(m):
    
    m = int(input())
    n = m
    a = []
    while 1 < m :
        m = m-1
        if n%m == 0:
            a.append(m)
    if len(a) == 2 :
        print(True)
    elif len(a) == 1:
        print(True)
    else:
        print(False)

def get_sum(start, end):
    number = 0
    for i in range(start, end+1):
        number = number + i
    return number

print(get_sum(3,11))
        

def get_factorial(n):
    number = n
    one = 1
    while number >1:
        one = number * one
        number = number -1
    return one

print(get_factorial(4))

def get_fact(n):
    fac = 1
    for end in range(1,n+1):
        fac = (fac*end)
    return fac
