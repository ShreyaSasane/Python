def Arthimatic(No1,No2):
    Ans = 0
    Ans = No1 + No2
    
    Sub = 0
    Sub = No1 - No2

    Mult = 0
    Mult = No1 * No2

    Div = 0
    Div = No1 / No2

    return Ans,Sub,Mult,Div

def main():
    Value = 0
    bRet1 = 0
    bRet2 = 0
    bRet3 = 0
    bRet4 = 0

    print("Enter the Number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    bRet1, bRet2, bRet3, bRet4 = Arthimatic(Value1, Value2)

    print("Addition is : ",bRet1)
    print("Substraction is : ",bRet2)
    print("Multiplication is : ",bRet3)
    print("Division is : ",bRet4)

if __name__ == "__main__":
    main()