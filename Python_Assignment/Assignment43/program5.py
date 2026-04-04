import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder

def PlayPredictor(DataPath):
    border = "-"*40

    ################################################################
    #
    #   Step 1: Load the CSV
    #
    ################################################################
    print(border)
    print("Step 1: Load the dataset from the CSV")
    print(border)

    df = pd.read_csv(DataPath)

    print("Some elements from the dataset")
    print(df.head())
    print(border)

    ################################################################
    #
    #   Step 2: Data Analysis (EDA)
    #
    ################################################################

    print(border)
    print("Step 2: Data Analysis (EDA)")
    print(border)

    print("shape of dataset : ",df.shape)
    print("Columns names : ",list(df.columns))

    print("missing values per column : ")
    print(df.isnull().sum())

    print("Class distribution : ")

    print(df["Play"].value_counts())

    print("Statistical Report of dataset :")
    print(df.describe())

    ################################################################
    #
    #   Step 3: Decide Independent And Dependent Variables
    #
    ################################################################

    print(border)
    print("Step 3: Decide Independent And Dependent Variables")
    print(border)

    Feature_cols = ["Whether",
                    "Temperature"]
    
    X = df[Feature_cols]

    Y = df["Play"]

    print("X shape : ",X.shape)
    print("Y shape : ",Y.shape)

    Encoded_x_Whether = LabelEncoder()
    Encoded_x_Temp = LabelEncoder()
    Encoded_Y = LabelEncoder()

    X['Whether'] = Encoded_x_Whether.fit_transform(X['Whether'])
    X['Temperature'] = Encoded_x_Temp.fit_transform(X['Temperature'])

    Y = Encoded_Y.fit_transform(Y)

    print("Mapping of labels are : ")
    print(Encoded_x_Whether.classes_)
    print(Encoded_x_Temp.classes_)
    print(Encoded_Y.classes_)


    ################################################################
    #
    #   Step 4: Split the dataset into training and testing
    #
    ################################################################

    print(border)
    print("Step 4: Split the dataset into training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42,stratify=Y,test_size=0.2)

    print(border)
    print("Information for training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ", Y_train.shape)
    print("Y_test shape : ",Y_test.shape)


    ################################################################
    #
    #   Step 5: Feature scaling
    #
    ################################################################

    print(border)
    print("Step 5: Feature scaling")
    print(border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scaling is done")

    ################################################################
    #
    #   Step 6: Explore the multiple values of K(hyperparameter tunning)
    #
    ################################################################

    print(border)
    print("Step 6: Explore the multiple values of K")
    print(border)

    accuracy_scores = []

    K_values = range(1,21)

    for K in K_values:

        model = KNeighborsClassifier(n_neighbors=K)

        model.fit(X_train_scaled,Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(accuracy)

        print(border)

        print("Accuracy report of all K values of 1 to 20")

        for value in accuracy_scores:
            
            print(value)

        print(border)

    #####################################################################
    #
    #   Step 7 : Plot graphn of K VS Accuracy
    #
    #####################################################################

    print(border)
    print("Step 7 : Plot graphn of K VS Accuracy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values, accuracy_scores,marker = 'o')
    plt.title("K values VS accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid()
    plt.xticks(list(K_values))
    plt.show()

    #####################################################################
    #
    #   Step 8 : Find best value of K
    #
    #####################################################################

    print(border)
    print("Step 8 : Find best value of K")
    print(border)

    best_K = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best values of K is : ",best_K)


    #####################################################################
    #
    #   Step 9 : Build final model using best value of K
    #
    #####################################################################

    print(border)
    print("Step 9 : Build final model using best value of K")
    print(border)

    Final_model = KNeighborsClassifier(n_neighbors=best_K)

    Final_model.fit(X_train_scaled,Y_train)

    Y_pred = Final_model.predict(X_test_scaled)

    #####################################################################
    #
    #   Step 10 : Calculate final accuracy
    #
    #####################################################################

    print(border)
    print("Step 10 : Calculate final accuracy")
    print(border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy od model is : ",accuracy*100)

    #####################################################################
    #
    #   Step 11 : Display confusion matrix
    #
    #####################################################################

    print(border)
    print("Step 11 : Display confusion matrix")
    print(border)

    cm = confusion_matrix(Y_test,Y_pred)

    print(cm)


    #####################################################################
    #
    #   Step 12 : Display classification report
    #
    #####################################################################

    print(border)
    print("Step 12 : Display classification report")
    print(border)

    print(classification_report(Y_test,Y_pred))
def main():
    border = "-"*40

    print(border)
    print("PlayPrictor using KNN")
    print(border)

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()