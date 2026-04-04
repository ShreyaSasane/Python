import os
import sys
def main():

    if((len(sys.argv) < 3) or (len(sys.argv) > 3)):
        print("Invalid number of arguments")
        return -1

    SourceFile = sys.argv[1]
    DestinationFile = sys.argv[2]

    Ret = os.path.exists(SourceFile)

    if(Ret == True):

        fobj = open(SourceFile,"r")

        Buffer = fobj.read()

        fobj = open(DestinationFile,"w")

        Data = fobj.write(Buffer)

        print("Data from the file is : ",Data)
        
    else:
        print("File is not exist in current directory")
        return -1
    
if __name__ == "__main__":
    main()