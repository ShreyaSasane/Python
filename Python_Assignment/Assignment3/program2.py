def CountDigit(iNo):
 
    iCnt = 0
    while(iNo != 0):
        iCnt = iCnt + 1
        iNo = iNo // 10
        
    return iCnt

def main():

    print("Enter the number : ")
    value = int(input())

    iRet = CountDigit(value)

    print("number of digits are : ",iRet)

    
if __name__ == "__main__":
    main()