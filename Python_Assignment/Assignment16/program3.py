def Add(no1, no2):
    Ans = 0
    Ans = no1 + no2
    return Ans
    
def main():

    Value1 = 0
    Value2 = 0
    iRet = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    iRet = Add(Value1, Value2)

    print("Addition is : ",iRet)
if __name__ == "__main__":
    main()