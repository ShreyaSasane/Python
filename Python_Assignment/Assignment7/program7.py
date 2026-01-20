String = lambda str : len(str) > 5      #here we compare length of string with 5

def main():
    value = 0

    print("Enter how many names you want to insert in list")
    value = int(input())

    names = []

    print("enter the elements")

    for i in range(value):
        names.append(input())

    FData = list(filter(String,names))
    print("Strings having length greater than 5 are  : ",FData)

if __name__ == "__main__":
    main()