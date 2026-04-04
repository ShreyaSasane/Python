import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def main():

    Border = "-"*50
    #################################################################
    #
    #   Step 1: Load the dataset
    #
    #################################################################

    df = pd.read_csv('student_performance_ml.csv')

    print(Border)
    print("Dataset is successfully loaded")
    print(Border)

    #################################################################
    #
    #   Step 2: Data Analysis 
    #
    #################################################################


    print("First 5 records from the dataset : ")
    print(df.head())

    print(Border)

    print("Shape of the dataset : ")
    print(df.shape)

    print(Border)

    print("last 5 records from the dataset")
    print(df.tail())

    print(Border)

    print("Column names from the dataset :")
    print(df.columns.to_list())

    print(Border)

    print("Data types of the columns :")
    print(df.dtypes)

    print(Border)

    TotalCount = len(df)
    print("Total number of students from the dataset :")
    print(TotalCount)

    print(Border)

    Passed = (df['FinalResult'] == 1).sum()
    Failed = (df['FinalResult'] == 0).sum()

    print("Total number of passed student : ")
    print(Passed)


    print("Total number of failed students : ")
    print(Failed)

    Study_Hours = df['StudyHours'].mean()
    print("Average study hours of the students :", Study_Hours)

    Attendance = df['Attendance'].mean()
    print("Average attendance of the students :", Attendance)

    Previous_Score = df['PreviousScore'].max()
    print("Maximum previous score of the students :", Previous_Score)

    Sleep_Hours = df['SleepHours'].min()
    print("Minimum sleep hours ", Sleep_Hours)

    print(Border)

    count = df['FinalResult'].value_counts()

    print("Distribution of final results :")
    print(count)

    PassStudentPercentage = Passed / TotalCount * 100
    FailStudentPercentage = Failed / TotalCount * 100

    print(Border)

    print("Percentage of passed students : ")
    print(PassStudentPercentage)

    print("Percentage of failed students : ")
    print(FailStudentPercentage)

    print("Statistical report of the dataset : ")
    print(df.describe())

    #################################################################
    #
    #   Step 3: Decide the features and target variable
    #
    #################################################################
    
    X = df[[             'StudyHours',
                        'Attendance',
                        'PreviousScore',
                        'PreviousScore',
                        'SleepHours'
            ]]
    
    Y = df['FinalResult']
    

    #################################################################
    #
    #   Step 4: Split the dataset into training and testing sets
    #
    #################################################################

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)
    print("Shape of the traing set :", X_train.shape)
    print("Shape of the testing set :", X_test.shape)

    #################################################################
    #
    #   Step 5: Scale the features
    #
    #################################################################

    Scaler = StandardScaler()
    X_Train_Scaled = Scaler.fit_transform(X_train)
    X_Test_Scaled = Scaler.transform(X_test)

    #################################################################
    #
    #   Step 5: Buildthe model
    #
    #################################################################

    Lr = LogisticRegression(random_state=42)


    #################################################################
    #
    #   Step 6: Train the model
    #
    #################################################################

    Lr.fit(X_Train_Scaled,Y_train)

    #################################################################
    #
    #   Step 7: Make the predictions
    #
    #################################################################

    Y_pred = Lr.predict(X_Test_Scaled)

    #################################################################
    #
    #   Step 8: Evaluate the model
    #
    #################################################################

    print("Classification Refort : ")
    print(classification_report(Y_test,Y_pred))

    print(Border)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred))

    print(Border)

    print("Accuracy score : ")
    print(accuracy_score(Y_test, Y_pred) * 100)

if __name__ == "__main__":
    main()

    #ValueError: Found input variables with inconsistent numbers of samples: [5, 30]