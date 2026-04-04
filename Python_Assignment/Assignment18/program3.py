def MinimumElement(Arr):
    Min = Arr[0]
    for i in range(len(Arr)):
        if (Arr[i] < Min):
            Min = Arr[i]
    return Min

def main(): 
    Value = 0

    print("Enter the number of elements that you want to insert in list :")
    Value = int(input())

    Arr = []

    print("Enter the elements into list : ")
    for i in range(0,Value,1):
        num = int(input())
        Arr = Arr + [num]


    iRet = MinimumElement(Arr)

    print("Minimum elements is : ",iRet)

if __name__ == "__main__":
    main()