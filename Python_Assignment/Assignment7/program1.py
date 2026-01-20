Square = lambda no : no * no

def main():
    value = 0

    print("Enter how many elements you want to insert in list")
    value = int(input())

    number = []

    print("enter the elements")

    for i in range(value):
        number.append(int(input()))

    MData = list(map(Square,number))
    print("square of each element is : ",MData)

if __name__ == "__main__":
    main()