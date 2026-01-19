def SumDigit(iNo):
    Sum = 0
    while(iNo != 0):
        iDigit = iNo % 10
        iNo = iNo // 10
        Sum = Sum + iDigit
    return Sum

def main():

    print("Enter the number : ")
    value = int(input())

    iRet = SumDigit(value)

    print("sum of digit is : ",iRet)

    
if __name__ == "__main__":
    main()