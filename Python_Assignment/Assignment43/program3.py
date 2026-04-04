import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 

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

def main():
    border = "-"*40

    print(border)
    print("PlayPrictor using KNN")
    print(border)

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()