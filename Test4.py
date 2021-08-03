
def distr__(n,m):
    a = []
    for i in range(n,m+1):
        List = list(str(i))
        if len(List) == 3:
            List_cal = int(List[0])*int(List[1])*int(List[2])
        elif len(List) == 2:
            List_cal = int(List[0])*int(List[1])
        a.append(List_cal)        
    print(sum(a))


distr__(10, 101)


sum=0
for n in range(10,101):
    part=1
    for i in str(n):
        part*=int(i)
    sum+=part
print(sum)


'''
