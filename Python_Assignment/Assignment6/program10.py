LargeNumber = lambda no1, no2, no3: no1 if no1 > no2 and no2 else no1 < no2 and no3  
def main():

    value1 = 0
    value2 = 0
    value3 = 0
    iRet = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    print("Enter second number : ")
    value3 = int(input())

    iRet =  LargeNumber(value1,value2,value3)

    print("Largest number is : ",iRet)
if __name__ == "__main__":
    main()