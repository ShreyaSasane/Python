def ChkNum(no):

    if(no > 0):
        print("Positive")
    elif(no < 0):
        print("Negative")
    else:
        print("Zero")
def main():

    Value = 0
    iRet = 0

    print("Enter the number : ")
    Value = int(input())

    ChkNum(Value)
if __name__ == "__main__":
    main()