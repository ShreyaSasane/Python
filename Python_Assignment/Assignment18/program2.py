def MaximumElement(Arr):
    Max = Arr[0]
    for i in range(len(Arr)):
        if (Arr[i] > Max):
            Max = Arr[i]
    return Max

def main(): 
    Value = 0

    print("Enter the number of elements that you want to insert in list :")
    Value = int(input())

    Arr = [0] * Value

    print("Enter the elements into list : ")
    for i in range(0,Value,1):
        num = int(input())
        Arr = Arr + [num]


    iRet = MaximumElement(Arr)

    print("Maximum elements is : ",iRet)

if __name__ == "__main__":
    main()