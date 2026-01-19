def ChkVowel(str):

    if(str == "a" or str == "e" or str == "i" or str == "o" or str == "u"):
        return True
    else:
        return False

def main():
    Value = 0
    bRet = False

    print("Enter the character : ")
    Value = input()

    bRet = ChkVowel(Value)

    if(bRet == True):
        print("It is a vowel")
    else:
        print("It is not a Vowel")

if __name__ == "__main__":
    main()