def ChkEven(no):
    
    for i in range(2,no + 1,2):
       print(i)
def main():
    value = 0
    iRet = 0

    value = (int(input("Enter the number : ")))

    ChkEven(value)
    
if __name__ == "__main__":
    main()