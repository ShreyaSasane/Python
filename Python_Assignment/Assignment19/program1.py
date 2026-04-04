PowerOfTwo = lambda no : 2**no

def main():
    
    print("Enter the number : ")
    Value = int(input())

    iRet = PowerOfTwo(Value)

    print(f"Power of two of the {Value} is : ",iRet)

if __name__ == "__main__":
    main()