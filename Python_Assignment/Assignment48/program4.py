from sklearn.preprocessing import StandardScaler
import math

def euclidean_distance(point1, point2):
    sum_of_squared_distance = 0
    for i in range(len(point1)):
        sum_of_squared_distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(sum_of_squared_distance)


def main():
    X = [
        [25, 20000],
        [30, 30000],
        [35, 40000]
    ]

    print("Distances BEFORE scaling:")
    for i in range(len(X)):

        for j in range(i+1, len(X)):

            distance = euclidean_distance(X[i], X[j])
            print(X[i], "to", X[j], "=", distance)

    scaler = StandardScaler()
    
    X_scaled = scaler.fit_transform(X)

    print("\nScaled Dataset:")
    print(X_scaled)

    print("\nDistances AFTER scaling:")
    for i in range(len(X_scaled)):

        for j in range(i+1, len(X_scaled)):

            distance = euclidean_distance(X_scaled[i], X_scaled[j])
            print(X_scaled[i], "to", X_scaled[j], "=", distance)


if __name__ == "__main__":
    main()