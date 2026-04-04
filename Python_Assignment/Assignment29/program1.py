import os
def main():

    print("Enter the file name : ")
    FileName = input()

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("File exist in current directory")
    else:
        print("File is not exist in current directory")
    
if __name__ == "__main__":
    main()