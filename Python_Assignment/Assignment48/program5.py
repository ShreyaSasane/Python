import numpy as np 
from sklearn.metrics import confusion_matrix

def main():
    Actual = np.array([1,1,1,1,0,0,0,0])
    Predicted = np.array([1,1,0,1,0,1,0,0])

    print("Actual : ",Actual)
    print("Predicted : ",Predicted)

    print("Confusion Matrix :")
    print(confusion_matrix(Actual,Predicted))
    
if __name__ == "__main__":
    main()