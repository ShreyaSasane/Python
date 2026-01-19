def FindFactor(iNo):
    iCnt = 0
    if(iNo // iCnt == 0):
        print(iCnt)


def main():
    Value = 0
    bRet = False

    print("Enter the Number : ")
    Value = int(input())

    FindFactor(Value)
if __name__ == "__main__":
    main()