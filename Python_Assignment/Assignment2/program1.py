def MultiplicationTbl(no):
    i = 0
    for i in range(1,11,1):
        print(i * no)


def main():
    value = 0
    iRet = 0

    value = (int(input("Enter the number of which you want a table : ")))

    MultiplicationTbl(value)

if __name__ == "__main__":
    main()