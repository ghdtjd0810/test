


n = 25
k = 4
result = 0
while True:
    if n == 1 : #n = 1이면
        break

    if n%k == 0: #나머지가 1이상이면
        n = n/k
        result += 1
            
    elif n%k != 0:
        n= n-1
        result += 1

            
print(n)
print(result)


n,k  = map(int, input().split())
result = 0

while n >=k:
    while n%k != 0:
        n -=1
        result += 1
    n//= k
    result += 1

print(result)



