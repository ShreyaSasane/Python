def CountDigit(iNo):
 
    while(iNo != 0):
        iDigit = iNo % 10
        print(iDigit)
        iNo = iNo // 10
def main():

    print("Enter the number : ")
    value = int(input())

    CountDigit(value)

    
if __name__ == "__main__":
    main()