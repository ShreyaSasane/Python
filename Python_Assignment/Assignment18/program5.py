from MarvellousNum import ChkPrime

def ListPrime(Arr):
    num = 0
    for i in range(len(Arr)):
        if ChkPrime(Arr[i]):
            print("prime numbers are : ",Arr[i])
            num =  num + Arr[i]
            
    return num



def main(): 
    Value = 0

    print("Enter the number of elements that you want to insert in list :")
    Value = int(input())
   
    Arr = []

    print("Enter the elements into list : ")
    for i in range(0,Value,1):
        num = int(input())
        Arr = Arr + [num]

    iRet = ListPrime(Arr)

    print("Addition of Prime number is : ",iRet)
    
if __name__ == "__main__":
    main()