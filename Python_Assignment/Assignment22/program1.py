class Demo:
    value = 0

    def __init__(self,No1,No2):
        self.a = No1
        self.b = No2

    def fun(self):
        print("instance variable from fun are  : ",self.a,self.b)

    def gun(self):
        print("instance variable from gun are  : ",self.a,self.b)


obj1 = Demo(11,21)
obj2 = Demo(10,20)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()

