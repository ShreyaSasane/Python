def ChkGreater(no1,no2):
    if(no1 > no2):
        return no1
    else:
        return no2
        

def main():
    value1 = 0
    value2 = 0
    iRet = 0

    value = (int(input("Enter first number:")))
    value2 = (int(input("Enter second number")))

    iRet = ChkGreater(value1,value2)

    print("Greater number is : ",iRet)

if __name__ == "__main__":
    main()