def ChkPrime(no):
    for i in range(2, int(no/2)+1):
        if(no % i == 0):
            return False
    return True

def main():

    bRet = False

    print("Enter the number : ")
    value = int(input())

    bRet = ChkPrime(value)

    if(bRet == True):
        print(value,"is a prime number")
    else:
        print(value,"is not a prime number")

if __name__ == "__main__":
    main()