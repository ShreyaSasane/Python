def ChkPalindrome(iNo):

    start = iNo
    end = 0
    while(iNo > 0):
        digit = iNo % 10
        end = end * 10 + digit
        iNo = iNo // 10
    if(start == end):
        return True
    else:
        return False
def main():
    value = 0

    print("Enter the number : ")
    value = int(input())

    bRet = ChkPalindrome(value)

    if(bRet == True):
        print("it is palindrome")
    else:
        print("it is not palindrome")
    
if __name__ == "__main__":
    main()