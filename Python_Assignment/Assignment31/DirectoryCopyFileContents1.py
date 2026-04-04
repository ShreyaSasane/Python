import sys
import os
import shutil

def DirectoryCopyContents(SourceDir,DestinationDir):

    if not os.path.exists(DestinationDir):
        os.mkdir(DestinationDir)

    Ret = ((os.path.isdir(SourceDir)) and (os.path.isdir(DestinationDir)))

    if(Ret == True):

        for FolderName, SubFolderName, FileName in os.walk(SourceDir):

            for Fname in FileName:
                
                Source = os.path.join(FolderName,Fname)
                Destination = os.path.join(DestinationDir,Fname)

                shutil.copy(Source, Destination)

                print(f"copied {Fname}")


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
            print("DirectoryName1 : Name of the directory from where you want to copy the contents")
            print("DirectoryName2 : Name of the directory where you want to paste that copied contents")
        else:
            print("Unable to procees as there is no such option")
            print("Please use --h or --u to get more details")

    #python program1.py Demo Hello
    elif(len(sys.argv) == 3):

        DirName1 = sys.argv[1]
        DirName2 = sys.argv[2]
    
        DirectoryCopyContents(DirName1,DirName2)

    else:
        print("Invalid number of command line arrguments")
        print("Unable to procees as there is no such option")
        print("Please use --h or --u to get more details")
    
    print(Border)
    print("---------Thank you for using out script-----------")
    print(Border)

if __name__ == "__main__":
    main()

    