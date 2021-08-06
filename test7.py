
try:
    fname = input('파일 이름을 입력하세요')
    infile = opem(fname,'r')
    
except 10Error:
    print('파일 발겭 할 수 없습니다')


try :
    rst <= 3/1
except ZeroDivisionError as e:
    print(e)
else:
    print(rst)
finally :
    print('계속')
    


try :
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
    


try:
    people= int(input('금액 입력'))
    pay = money/people
    print(pay,'원씩 나누어 주세요')
except ValueError as e:
    print('숫자만 입력 가능')
except ZeroDivisionError as e:
    print('인원 은 1명 이상이ㅓㅇ야 함')
    


sum = 0
while True:
    try:
        num = int(input('숫자입력'))
        sum += num
        print(sum)
    except ValueError as e:
        print('숫자외 아ㅇ;ㅂ려ㅑㄱ')
        print('합', sum)
        break


sum = 0
try:
    fh = open('t.txt', 'w')
    while True:
        try:
            num = int(input('숫자입력'))
            if num == 0:
                fh.write('합' + str(num))
                break
            elif num%3 ==0:
                fh.write(str(num)+'\n')
                sum += num
        except ValueError as e:
            print('숫자 외 입력')
except IOError as e:
    print('파일 생성 못했음')

finally:
    fh.close()
    

        