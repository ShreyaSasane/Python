def main():
    print("Enter the file Name : ")
    Fname = input()

    fobj = open(Fname,"r")

    Data = fobj.read()

    fobj.close()

    print(f"Contents from the {Fname} are :\n",Data)

if __name__ == "__main__":
    main()