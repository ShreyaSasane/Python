from functools import reduce

def ChkPrime(no):
    if no <= 1:
        return False
    
    for i in range(2, int(no/2) + 1,1):
        if no % i == 0:
            return False
        
    return True

Multiply  = lambda no:  no * 2
   
def Max(No1,No2):
    if(No1 > No2):
        return No1
    else:
        return No2

def main():
    
    print("Enter how many elements you want to enter in List : ")
    Value = int(input())

    Data = []

    print("Enter the Elements into the list")
    for i in range(Value):
        
        num = int(input())
        Data = Data + [num]


    FData = list(filter(ChkPrime,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Multiply,FData))
    print("Data after Map is : ",MData)

    RData = reduce(Max,MData)
    
    print("Data after Reduce is : ",RData)




    


if __name__ == "__main__":
    main()