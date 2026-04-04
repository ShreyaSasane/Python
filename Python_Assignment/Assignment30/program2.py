def main():
    print("Enter the file Name : ")
    Fname = input()

    fobj = open(Fname,"r")

    Data = fobj.read()

    Count = 0
    Ch = False

    for word in Data:
        if(word != " " and word != "\n"):
           if Ch == False:
               Count = Count + 1
               Ch = True
        else:
           Ch = False
        
    fobj.close()

    print(f"Total number of words in {Fname} is : ",Count)

if __name__ == "__main__":
    main()