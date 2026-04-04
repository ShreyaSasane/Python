import os

def main():
    print("Enter the Existing file Name : ")
    SourceFile = input()

    print("Enter the new file Name to copy the data : ")
    DestinationFile = input()

    Ret = os.path.exists(SourceFile)

    if(Ret == True):

        fobj = open(SourceFile,"r")

        Data = fobj.read()

        fobj = open(DestinationFile,"w")

        Buffer = fobj.write(Data)

    else:
        print("There is no such file exits")
        print("Please give Existing file")
        
    fobj.close()

    print(f"{SourceFile} contents are susscessfuly copied to the {DestinationFile}",Buffer)

if __name__ == "__main__":
    main()