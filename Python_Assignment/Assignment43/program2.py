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
    
def main():
    border = "-"*40

    print(border)
    print("PlayPrictor using KNN")
    print(border)

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()