import os
import sys
def main():

    if((len(sys.argv) < 3) or (len(sys.argv) > 3)):
        print("Invalid number of arguments")
        return -1

    SourceFile = sys.argv[1]
    DestinationFile = sys.argv[2]

    Ret = ((os.path.exists(SourceFile)) and (os.path.exists(DestinationFile)))

    if(Ret == True):

        fobj = open(SourceFile,"r")

        Buffer = fobj.read()

        fobj = open(DestinationFile,"r")

        Data = fobj.read()

        if(Buffer == Data):
            print("Success")
        else:
            print("Failure")
        
    else:
        print("File is not exist in current directory")
        return -1
    
if __name__ == "__main__":
    main()