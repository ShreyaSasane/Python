pi = 3.14

def FindAreaCircle(radius):
    Area = 0
    Area = pi * radius * radius
    return Area


def main():
    Value1 = 0
    iRet = 0

    print("Enter the radius : ")
    Value1 = int(input())

    iRet = FindAreaCircle(Value1)

    print("Area of circle is : ",iRet)

if __name__ == "__main__":
    main()