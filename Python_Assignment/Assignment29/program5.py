
def main():

    print("Enter the file name : ")
    fname = input()

    print("Enter the string : ")
    string = input()

    fobj = open(fname,"r")
    Data = fobj.read()

    Count = 0
    StringLength = len(string)

    for i in range(len(Data)):
        if(Data[i: i + StringLength]== string):
            Count = Count + 1

    print(f"{string} appears in the file :",Count)
    
if __name__ == "__main__":
    main()