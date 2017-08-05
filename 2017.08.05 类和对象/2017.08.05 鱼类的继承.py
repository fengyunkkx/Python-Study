import random as r

class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置在：",self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有得吃！")
            self.hungry = False
        else:
            print("太撑了，吃不下了")

'''
测试
>>> fish = Fish()
>>> #试试看小鱼能不能移动
>>> fish.move()
我的位置在： 6 3
>>> goldfish = Goldfish()
>>> goldfish.move()
我的位置在： 1 7
>>> goldfish.move()
我的位置在： 0 7
>>> goldfish.move()
我的位置在： -1 7
>>>
>>> #可见金鱼确实是在一路向西
>>>
>>>
>>> #下面生成鲨鱼
>>> shark = Shark()
>>> # 试试看能不能吃东西
>>> shark.eat()
吃货的梦想就是天天有得吃！
>>> shark.move()
我的位置在： 9 3
>>> shark.move()
我的位置在： 8 3
>>>



'''
