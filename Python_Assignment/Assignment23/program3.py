class Numbers:

    def __init__(self):
        self.Value = int(input("Enter the number : "))

    def ChkPrime(self):
        if(self.Value < 1):
            return False
        else:
            for i in range(2,int(self.Value//2) + 1):
                 if(self.Value % i == 0):
                     return False
                 
            return True

    def ChkPerfect(self):

        if(self.Value <= 1):
            return False
        
        icnt = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                icnt += i

        return icnt == self.Value

    def Factors(self):
        for i in range(1,self.Value,1):
            if(self.Value % i == 0):
                print(f"Factors of the {self.Value} are : ",i)

    def SumFactor(self):
        sum = 0
        for i in range(1,self.Value,1):
            if(self.Value % i == 0):
               sum = sum  + i
        return sum
        

obj = Numbers()

pRet = obj.ChkPrime()

if(pRet == True):
    print("it is prime number")
else:
    print("it is not a prime number")

cRet = obj.ChkPerfect()

if(cRet == True):
    print("It is a perfect number")
else:
    print("It is not perfect number")

fobj = obj.Factors()

sobj = obj.SumFactor()

print("Sum of factors is : ",sobj)