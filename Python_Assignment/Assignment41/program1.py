
#  Col     [A,B,C,D]
#   X      [1,2,3,5]
#   Y      [2,3,1,6]
# Result   [Red,Red,Blue,Blue]

#To predict (X = 3, Y = 3) -> ?     (Blue/Red)
import numpy as np
import math

def EucDistance(P1, P2):
    Ans = math.sqrt(((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2))

    return Ans

def MarvellousKNighborsClassifier():
    border = "-"*40
    data =  [   {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
                {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
                {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
                {'point' : 'D', 'X' : 5, 'Y' : 6, 'label' : 'Blue'}
            ]
    
    print(border)
    print("--------Marvellous UserDefined KNN--------")
    print(border)

    print(border)
    print("Traing Data Set")
    print(border)

    for i in data:
        print(i)

    print(border)

    new_point = {'X' : 3, 'Y' : 3}      #point for testing

    #Calculate all distances
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(border)
    print("Calculated distances are : ")
    print(border)

    for d in data:
        print(d)

    sorted_data = sorted(data,key=lambda item : item['distance'])

    print(border)
    print("Sorted data is : ")
    print(border)

    for d in sorted_data:
        print(d)

    K = 3

    nearest = sorted_data[:K]

    print(border)
    print("Nearest 3 element are : ")
    print(border)

    for d in nearest:
        print(d)

    #Voting
    votes = {}
   
    for neighbor in nearest:
        label = neighbor['label']
        votes[label] = votes.get(label,0) + 1

    print(border)
    print("Voting result is : ")
    print(border)

    for d in votes:
        print("Name : ",d, "Number of votes: ",votes[d])

    print(border)

def main():

    MarvellousKNighborsClassifier()

if __name__ == "__main__":
    main()