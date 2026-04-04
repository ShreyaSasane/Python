def Display(no):

    for i in range(1,no+1,1):
        print("*")
    
def main():

    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)
if __name__ == "__main__":
    main()