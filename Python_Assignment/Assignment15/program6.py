from functools import reduce

Maximum = lambda no1,no2 :  no1 if no1 < no2 else no2
def main():
    value = 0

    print("Enter how many elements you want to insert in list")
    value = int(input())

    number = []

    print("enter the elements")

    for i in range(value):
        number.append(int(input()))

    RData = reduce(Maximum,number)
    print("Minimum elements in the list: ",RData)

if __name__ == "__main__":
    main()