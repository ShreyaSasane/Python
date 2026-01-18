def ChkSquare(no):
    Ans = 0
    Ans = no*no
    return Ans

def main():
    value = 0

    value = (int(input("Enter number:")))

    iRet = ChkSquare(value)
 
    print("Square of",value,":",iRet)

if __name__ == "__main__":
    main()