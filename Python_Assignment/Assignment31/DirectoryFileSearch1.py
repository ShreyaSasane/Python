import sys
import os
import time
import schedule

def SearchFileExtension(DirName,Extension):

    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for Fname in FileName:
            if(Fname.endswith(Extension)):
                print(Fname)

def main():
    
    Border = "-"*50
    print(Border)
    print("---------File Extension Scanner---------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to : ")
            print("display all the file with the extension given by the user")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print("ScriptName.py : The script that you are running ")
            print("DirectoryName : Name of the directory where you want to search files")
            print("Extension(example : .txt) : The file extension that you want to search")
        else:
            print("Unable to procees as there is no such option")
            print("Please use --h or --u to get more details")

    #python program1.py Demo .txt
    elif(len(sys.argv) == 3):

        DirName = sys.argv[1]
        Extension = sys.argv[2]

        SearchFileExtension(DirName,Extension)

    else:
        print("Invalid number of command line arrguments")
        print("Unable to procees as there is no such option")
        print("Please use --h or --u to get more details")
    
    print(Border)
    print("---------Thank you for using out script-----------")
    print(Border)

if __name__ == "__main__":
    main()

    