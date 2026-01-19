def FindArea(length,width):
    Area = 0
    Area = length * width
    return Area


def main():
    Value1 = 0
    Value2 = 0
    iRet = 0

    print("Enter the lenght : ")
    Value1 = int(input())

    print("Enter the width : ")
    Value2 = int(input())

    iRet = FindArea(Value1,Value2)

    print("Area of rectangle is : ",iRet)

if __name__ == "__main__":
    main()