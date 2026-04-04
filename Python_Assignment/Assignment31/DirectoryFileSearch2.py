import sys
import os
import time
import schedule

def SearchFileExtensionRename(DirName,Extension1, Extension2):
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):

        for Fname in FileName:
            if(Fname.endswith(Extension1)):

                O_path = os.path.join(FolderName,Fname)
                
                NewName = Fname.replace(Extension1,Extension2)

                N_path = os.path.join(FolderName,NewName)

                os.rename(O_path,N_path)

                print(f"remaned {O_path} with {N_path}")

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
            print("Extension(example : .log) : The file extension that you want to replace")
        else:
            print("Unable to procees as there is no such option")
            print("Please use --h or --u to get more details")

    #python program1.py Demo .txt .log
    elif(len(sys.argv) == 4):

        DirName = sys.argv[1]
        Extension1 = sys.argv[2]
        Extension2 = sys.argv[3]

        SearchFileExtensionRename(DirName,Extension1,Extension2)

    else:
        print("Invalid number of command line arrguments")
        print("Unable to procees as there is no such option")
        print("Please use --h or --u to get more details")
    
    print(Border)
    print("---------Thank you for using out script-----------")
    print(Border)

if __name__ == "__main__":
    main()

    