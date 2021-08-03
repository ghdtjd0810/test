@ -1,39 +1,4 @@
def  getTotalPage(m,n):
    if m% n == 0:
        return m//n
    else:
        return m // n+1
n,m = input().split()

print(getTotalPage(5,10))

m = int(input('게시글수 :' ))
n = 10

if m  % n ==0 :
    number = m//n
    print(number)
else :
    number = m//n 
    print(number + 1)


scores = [90,85, 77, 65, 97]
for i in range(5):
    if scores[i] >= 80:
        print(i + 1, '번 학생은 합격입니다.')

    
m=int(input("게시물(m)의 수 : "))
n=int(input("페이지당 게시물(n)의 수 : "))

if (m%n) > 0:
    page=m/n+1
elif (m%n) == 0: page=m/n
print("m =",m, "| n =",n,"| page =",int(page))

a = 0
m = 0
while m < 10:
    m += 1
    a = m + a
print(a)
