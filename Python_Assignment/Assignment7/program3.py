Even = lambda no : (no % 2 != 0)

def main():
    value = 0

    print("Enter how many elements you want to insert in list")
    value = int(input())

    number = []

    print("enter the elements")

    for i in range(value):
        number.append(int(input()))

    FData = list(filter(Even,number))
    print("Odd elements in the list are : ",FData)

if __name__ == "__main__":
    main()