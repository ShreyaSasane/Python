from functools import reduce

ChkEven = lambda no:  no % 2 == 0
Increament = lambda no:  no * no
   
Add = lambda A,B : A + B

def main():
    
    print("Enter how many elements you want to enter in List : ")
    Value = int(input())

    Data = []

    print("Enter the Elements into the list")
    for i in range(Value):
        
        num = int(input())
        Data = Data + [num]


    FData = list(filter(ChkEven,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increament,FData))
    print("Data after Map is : ",MData)

    RData = reduce(Add,MData)
    print("Data after Reduce is : ",RData)




    


if __name__ == "__main__":
    main()