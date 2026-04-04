def AddOfElements(Arr):
    Add = 0
    for i in Arr:
        
        Add = Add + i

    return Add


def main():
    Value = 0

    print("Enter the number of elements that you want to insert in list :")
    Value = int(input())

    Arr = [0] * Value

    print("Enter the elements into list : ")
    for i in range(0,Value,1):
        num = int(input())
        Arr = Arr + [num]


    iRet = AddOfElements(Arr)

    print("Addition of elements is : ",iRet)

if __name__ == "__main__":
    main()