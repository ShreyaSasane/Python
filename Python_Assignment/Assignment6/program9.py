Mult = lambda no1, no2: (no1 * no2)

def main():

    value1 = 0
    value2 = 0
    iRet = 0

    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    iRet =  Mult(value1,value2)

    print("Multiplication is : ",iRet)
if __name__ == "__main__":
    main()