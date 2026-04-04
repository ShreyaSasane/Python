def main():
    print("Enter the file Name : ")
    Fname = input()

    fobj = open(Fname,"r")

    Data = fobj.read()

    Count = 0
    for ch in Data:
        if(ch == "\n"):
            Count = Count + 1
    
    fobj.close()

    print(f"Total number of lines in {Fname} is : ",Count)

if __name__ == "__main__":
    main()