class Arithmatic:
    
    def __init__(self):
        self.value1 = 0
        self.value2 = 0


    def Accept(self):
        self.value1 = int(input("Enter first value : "))
        self.value2 = int(input("Enter second value : "))

    def Addition(self):
        Add = 0
        Add = self.value1 + self.value2
        return Add
    
    def Substraction(self):
        Sub = 0
        Sub = self.value1 - self.value2
        return Sub
        
    def Division(self):
        Div = 0
        Div = self.value1 / self.value2
        return Div
    
    def Multiplication(self):
        Mult = 0
        Mult = self.value1 * self.value2
        return Mult
    

aobj = Arithmatic()

aobj.Accept()

iRet = aobj.Addition()
print("Addition is : ",iRet)

iRet = aobj.Substraction()
print("Substraction is : ",iRet)

iRet = aobj.Multiplication()
print("Multiplication is : ",iRet)

iRet = aobj.Division()
print("Division is : ",iRet)