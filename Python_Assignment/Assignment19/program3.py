from functools import reduce

ChkNumber = lambda no:  no >=70 and no <=90

Increament = lambda no:  no + 10
   
Mult = lambda A,B : A * B

def main():
    
    print("Enter how many elements you want to enter in List : ")
    Value = int(input())

    Data = []

    print("Enter the Elements into the list")
    for i in range(Value + 1):
        
        num = int(input())
        Data = Data + [num]


    FData = list(filter(ChkNumber,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increament,FData))
    print("Data after Map is : ",MData)

    RData = reduce(Mult,MData)
    print("Data after Reduce is : ",RData)




    


if __name__ == "__main__":
    main()