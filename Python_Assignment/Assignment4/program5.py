def Number(no):

    for i in range(no,0,-1):
        print(i)

def main():
    Value = 0

    print("Enter the Number : ")
    Value1 = int(input())

    Number(Value1)
    
if __name__ == "__main__":
    main()