ChkDivisible = lambda no : (no % 3 == 0) and (no % 5 == 0)

def main():
    value = 0

    print("Enter how many elements you want to insert in list")
    value = int(input())

    number = []

    print("enter the elements")

    for i in range(value):
        number.append(int(input()))

    FData = list(filter(ChkDivisible,number))
    print("Number is divisible by 5 and 3 are : ",FData)

if __name__ == "__main__":
    main()