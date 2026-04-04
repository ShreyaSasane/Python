import os

def main():
    print("Enter the Existing file Name : ")
    Fname = input()

    print("Enter the word that you want to search")
    Word = input()

    Ret = os.path.exists(Fname)

    if(Ret == True):

        fobj = open(Fname,"r")

        Data = fobj.read()

        if Word in Data:
            print(f"{Word} is present in {Fname}")
        else:
            print(f"{Word} is not present in {Fname}")
    else:
        print("There is no such file exits")
        print("Please give Existing file")
        
    fobj.close()
if __name__ == "__main__":
    main()