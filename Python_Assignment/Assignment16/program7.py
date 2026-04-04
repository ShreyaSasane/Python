def ChkDivisible(no):
    if(no % 5 == 0):
        return True
    else:
        return False
def main():

    Value = 0
    iRet = 0

    print("Enter the number : ")
    Value = int(input())

    iRet = ChkDivisible(Value)

    if(iRet == True):
        print(iRet)
    else:
        print(iRet)
if __name__ == "__main__":
    main()