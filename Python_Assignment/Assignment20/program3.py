import threading
import time

def Even(no):
    sum = 0
    for i in range(2,no + 1):
        if(i % 2 == 0):
            sum = sum + i
    return sum

def Odd(no):
    odd = 0
    for i in range(2, no + 1):
        if(i % 2 != 0):
            odd = odd + i
    return odd

def main():

    print("Enter the number of values you want to store in list")
    No = int(input())

    Value = []

    print("Enter the elements into the string : ")
    for i in range(No):
        num = int(input())
        Value = Value + [num[i]]

    start_time = time.time()

    t1 = threading.Thread(target = Even,args = (Value,))

    t2 = threading.Thread(target = Odd, args = (Value,))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

    print("Total execution time is : ",end_time - start_time)
if __name__ == "__main__":
    main()