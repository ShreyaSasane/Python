Max = lambda no1, no2 : no1 if no1 > no2 else no2

def main():

    value1 = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    bRet =  Max(value1,value2)

    print("maximum number is : ",bRet)

if __name__ == "__main__":
    main()