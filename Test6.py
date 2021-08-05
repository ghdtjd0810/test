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


class radius:
    def __init__(self, r):
        self.r = r
        

    def wide(self):
        
        return 3.14*self.r*self.r

    def side(self):
        return 2*3.14*self.r
a = radius(4)

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


class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print(self.name)
        print(self.age)

a = Cat('Missy', 3)
a.call()
class Box():
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def voulme(self):
        return self.width* self.height*self.depth
        
a = Box(15,14,13)
print(a.voulme())

