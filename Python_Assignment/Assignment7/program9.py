from functools import reduce

Product = lambda no1,no2 :  no1 * no2
def main():
    value = 0

    print("Enter how many elements you want to insert in list")
    value = int(input())

    number = []

    print("enter the elements")

    for i in range(value):
        number.append(int(input()))

    RData = reduce(Product,number)
    print("Product of all elements in list is ",RData)

if __name__ == "__main__":
    main()