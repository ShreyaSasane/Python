import os
import sys
import hashlib
import errno
import time

def CheckSum(FileName):

    try:
        fobj = open(FileName,"rb")

        hobj = hashlib.md5()

        Buffer = fobj.read(1024)

        while(len(Buffer) > 0):
            hobj.update(Buffer)
            Buffer = fobj.read(1024)

        fobj.close()

        return hobj.hexdigest()
    
    except OSError as e:
        print(f"Error: {FileName}")
        print(os.strerror(e.errno))   # Equivalent to perror
        return None



def DirectoryWatcher(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Chksum = CheckSum(fname)
                
            Boarder = "-"*50
            TimeStamp = time.ctime()

            #Gives FileName in the format  name of the file,day,month,date,hour,min,sec,year
            # "Marvellous_Sun_Feb_1_19_01_03_2026"
            LogFileName = "Marvellous%s.log" %(TimeStamp)
            LogFileName = LogFileName.replace(" ","_")
            LogFileName = LogFileName.replace(":","_")
            fobj = open(LogFileName,"w")

            




def main():
    
    Border = "-"*50
    print(Border)
    print("-------------Directory Scanner-------------")
    print(Border)

    if(len(sys.argv) == 1):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to : ")
            print("display the CheckSum of all files")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print("ScriptName.py : The script that you are running ")
            print("DirectoryName : Give the directory name of which you want to checksum")
        else:
            print("Unable to procees as there is no such option")
            print("Please use --h or --u to get more details")

    #python program1.py Demo 
    elif(len(sys.argv) == 2):

        DirName = sys.argv[1]
    
        DirectoryWatcher(DirName)

    else:
        print("Invalid number of command line arrguments")
        print("Unable to procees as there is no such option")
        print("Please use --h or --u to get more details")
    
    print(Border)
    print("---------Thank you for using out script-----------")
    print(Border)

if __name__ == "__main__":
    main()

    