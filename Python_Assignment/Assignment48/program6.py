import numpy as np 
from sklearn.metrics import classification_report

def main():
    Actual = np.array([1,1,1,1,0,0,0,0])
    Predicted = np.array([1,1,0,1,0,1,0,0])

    print("Actual : ",Actual)
    print("Predicted : ",Predicted)

    print("Classification Report : ")
    print(classification_report(Actual,Predicted))
    
if __name__ == "__main__":
    main()