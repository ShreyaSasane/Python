
def Display(no):
    Marks = no

    if(Marks >= 75):
        print("Distinction")
    elif(Marks >= 60):
        print("First class")
    elif(Marks >= 50):
        print("Second class")
    elif(Marks < 50):
        print("fail")


def main():
    Value1 = 0

    print("Enter the Marks : ")
    Value1 = int(input())

    Display(Value1)

if __name__ == "__main__":
    main()