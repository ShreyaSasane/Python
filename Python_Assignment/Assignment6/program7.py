Dvisible = lambda no1: (no1 % 5 == 0)

def main():

    value1 = 0
    bRet = False

    print("Enter first number : ")
    value1 = int(input())

    bRet =  Dvisible(value1)

    if(bRet == True):
        print("True : Number is divisible by 5")
    else:
       print("False : Number is not divisible by 5")

if __name__ == "__main__":
    main()