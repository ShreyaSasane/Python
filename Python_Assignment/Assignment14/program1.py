Square = lambda no : no * no

def main():

    value = 0
    bRet = False

    print("Enter the number : ")
    value = int(input())

    bRet =  Square(value)

    print("square of ",value,"is : ",bRet)

if __name__ == "__main__":
    main()