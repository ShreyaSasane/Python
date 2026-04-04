import pandas as pd
from sklearn.preprocessing import LabelEncoder

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


def main():
    border = "-"*40

    print(border)
    print("PlayPrictor using KNN")
    print(border)

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()