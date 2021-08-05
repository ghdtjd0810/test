'''
class Rectangle:
    def __init__(self, side=0, num =0):
        self.side = side

    def getArea(self):
        return self.side*self.side



def printAreas(r, n):
    while n>=1:
        print(r.side, r.getArea())
        r.side = r.side +1
        n = n-1

a = Rectangle()
count = 5
printAreas(a, count)

class Circle:
    def __init__(self, radius):# 초기화 하려면  r에다가 10을 넣으면 될 듯
        self.radius = radius
    def setRadius(self,r):
        self.radius = r
    def getRadius(self):
        return self.radius
    
    def wide(self):
        area = 3.14*self.radius * self.radius
        return area

    def side(self):
        return 2*3.14*self.radius

a = Circle(4)

print(a.wide())
print(a.side())




class Balance():
    def __init__(self, money):
        self.money = money

    def withdraw(self):
        print("통장에서", self.money, "가 출금되었음")
    def deposit(self):
        print('통장에', self.money, '가 입금됌')

a = Balance(100)
a.withdraw()
a.deposit()


class Bank:
    def __init__(self, balance = 0): # 초기화가 있으면 setbalance 하는게 좋다하시는데?
        self.balance = balance
    def setBalance(self, b):
        self.balance = b
    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            print('출금이 안됌')
        else:
            self.balance -= amount
            print('통장에서', self.balance, '만큼 출금됌')

    def deposit(self, amount):
        self.balance += amount
        print('잔액', self.balance)

a = Bank(0)#뺑크 하나 만들고 초기값 설정
a.deposit(10)# 입금하면서 10 느는건데, amount = 10으로 함수 받음
a.deposit(20)
a.withdraw(5)# 얘도 balance에다가 5를 출금 하는 형태, 즉 amount르ㅗ 함수 받음

'''
        
# 내 
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print(self.name)
        print(self.age)

a = Cat('Missy', 3)
b = Cat('Lucky', 5)

a.call()
b.call()

# 여기는 교수님 해답 
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age


class Box():
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def voulme(self):
        return self.width* self.height*self.depth
        
a = Box(15,14,13)
print(a.voulme())

