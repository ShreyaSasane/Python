def ChkNum(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def main():

    Value = 0
    iRet = 0

    print("Enter the number : ")
    Value = int(input())

    iRet = ChkNum(Value)

    if(iRet == True):
        print("Even Number")
    else:
        print("Odd Number")
if __name__ == "__main__":
    main()