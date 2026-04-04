Multipliction = lambda no1,no2: no1 * no2

def main():
    
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    iRet = Multipliction(Value1,Value2)

    print("Multiplication is ",iRet)

if __name__ == "__main__":
    main()