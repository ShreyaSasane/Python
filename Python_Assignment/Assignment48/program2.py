import numpy as np

def main():
    X = np.array([6,7,8,9,10,11,12])
    
    mean_Value = np.mean(X)

    print("Mean : ",mean_Value)

    Deviation_from_Mean = X - mean_Value
    
    print(Deviation_from_Mean)

    Squared_Deviation = Deviation_from_Mean ** 2
    
    print("Sum of Squared : ",Squared_Deviation)

    Sum_of_Squared_Deviation = np.sum(Squared_Deviation)

    print("Sum of Squared Deviation :",Sum_of_Squared_Deviation)

    Variance = Sum_of_Squared_Deviation / len(X)

    print("Variance : ",Variance)

    print("Standard Deviation : ",np.sqrt(Variance))


if __name__ == "__main__":
    main()