even = lambda no1: (no1 % 2 == 0)

def main():

    value1 = 0
    bRet = False

    print("Enter first number : ")
    value1 = int(input())

    bRet =  even(value1)

    if(bRet == True):
        print("Number is even : True")
    else:
       print("Number is even : False")
if __name__ == "__main__":
    main()