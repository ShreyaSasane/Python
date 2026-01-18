def ChkDivisible(no):
    if((no % 3 == 0)&(no % 5 == 0)):
        return True
    else:
        return False
def main():
    value = 0
    bRet = False
    value = (int(input("Enter number:")))

    bRet = ChkDivisible(value)

    if(bRet == True):
        print(value,"is divisible by 3 and 5")
    else:
        print(value,"is not divisible by 3 and 5")
 
    
if __name__ == "__main__":
    main()