Cube = lambda no : no ** 3

def main():

    value = 0
    bRet = False

    print("Enter the number : ")
    value = int(input())

    bRet =  Cube(value)

    print("Cube of ",value,"is : ",bRet)

if __name__ == "__main__":
    main()