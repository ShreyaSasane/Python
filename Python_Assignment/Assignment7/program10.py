CountEven = lambda no : no % 2 == 0 

def main():
    value = 0

    print("Enter how many elements you want to insert in list")
    value = int(input())

    number = []

    print("enter the elements")

    for i in range(value):
        number.append(int(input()))

    FData = list(filter(CountEven,number))

    print("Count of even number in the list : ",len(FData))

if __name__ == "__main__":
    main()