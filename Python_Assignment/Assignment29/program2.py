import os
def main():

    print("Enter the file name : ")
    FileName = input()

    Ret = os.path.exists(FileName)

    if(Ret == True):

        fobj = open(FileName,"r")

        Buffer = fobj.read()

        print("Data from the file is : ",Buffer)
        
    else:
        print("File is not exist in current directory")
    
if __name__ == "__main__":
    main()