Minimum = lambda no1, no2 : no1 if no2 > no1 else no2

def main():

    value1 = 0
    iRet = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    iRet =  Minimum(value1,value2)

    print("minimum number is : ",iRet)

if __name__ == "__main__":
    main()