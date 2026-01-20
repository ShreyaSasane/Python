from functools import reduce

Addition = lambda A,B :  A + B
def main():
    value = 0

    print("Enter how many elements you want to insert in list")
    value = int(input())

    number = []

    print("enter the elements")

    for i in range(value):
        number.append(int(input()))

    RData = reduce(Addition,number)
    print("Addition of all elements in the list: ",RData)

if __name__ == "__main__":
    main()