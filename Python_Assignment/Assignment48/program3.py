#print the scaled dataset using Standard scaler

from sklearn.preprocessing import StandardScaler

def main():
    X = [   [ 25, 20000], 
            [30, 30000], 
            [35, 40000]
        ]

    Scaler = StandardScaler()

    X_Scaled = Scaler.fit_transform(X)

    print("Scaled Dataset : ")
    print(X_Scaled)

if __name__ == "__main__":
    main()