def Summation(no):
    ans = 0
    for i in range(1,no + 1):
        ans = ans + i
    return ans
def main():
    value = 0
    iRet = 0

    value = (int(input("Enter the number : ")))

    iRet = Summation(value)

    print(iRet)
if __name__ == "__main__":
    main()

    