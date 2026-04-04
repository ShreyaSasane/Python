def SearchFrequence(Arr,No):
    iCnt = 0
    for i in range(len(Arr)):
        if(Arr[i] == No):
            iCnt += 1
    return iCnt


def main(): 
    Value = 0

    print("Enter the number of elements that you want to insert in list :")
    Value = int(input())

    Arr = []

    print("Enter the elements into list : ")
    for i in range(0,Value,1):
        num = int(input())
        Arr = Arr + [num]

    print("Enter the element that you want to search from list")
    Search = int(input())

    iRet = SearchFrequence(Arr,Search)

    print(f"frequence of {Search} is : ",iRet)

if __name__ == "__main__":
    main()