
def ChkPerfect(no):
    Sum = 0

    for i in range(1,int(no//2)+1):
        if(no % i == 0):
            Sum = Sum + i
    
    if(Sum == no and no > 0):
        return True
    else:
        return False

def main():
    Value1 = 0
    iRet = 0

    print("Enter the number : ")
    Value1 = int(input())

    iRet = ChkPerfect(Value1)

    if(iRet == True):
        print("It is a perfect number")
    else:
        print("It is not a perfect number")

if __name__ == "__main__":
    main()