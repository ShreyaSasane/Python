def ChkCube(no):
    Ans = 0
    Ans = no**3
    return Ans

def main():
    value = 0

    value = (int(input("Enter number:")))

    iRet = ChkCube(value)
 
    print("Cube of",value,":",iRet)

if __name__ == "__main__":
    main()