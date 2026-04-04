from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#Load the dataset

df = pd.read_csv("Advertising.csv")

print("Shape of dataset :",df.shape)
print("First 5 recods : ")
print(df.head())

#remove Unamed columns
if 'Unnamed: 0' in df.columns:

    df.drop(columns= ['Unnamed : 0'], inplace= True)
    
print("Shape of dataset : ")
print(df.shape)

print(df.tail())


#check missing

print("Missing value count : ")
print(df.isnull().sum())

#Display statistical report 

print(df.describe())

#Correlation between columns

print("Correlation between columns :")
print(df.corr())

#Split Indepndent and dependent variables

X = df[['TV','radio','newspaper']]

Y = df['sales']

#Split the data into training and testing 

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#Create the base model

base_model = DecisionTreeRegressor(random_state= 42)

#Create Bagging model

Bagging_model = BaggingRegressor(
                                    estimator=base_model,
                                    n_estimators=10,
                                    random_state=42
                                )

#train the model

Bagging_model.fit(X_train, Y_train)

#predict

Y_pred = Bagging_model.predict(X_test)

#Evaluate

print("Mean Squared error : ", mean_squared_error(Y_test, Y_pred) * 100)
print("R2 score : ", r2_score(Y_test, Y_pred) * 100)

#Compare the actual and predicted 

Result = pd.DataFrame({'Actual sale' : Y_test.values,
                        'Predicted sale' : Y_pred
                        })

print(Result.head())

#Plot the actual VS Predicted 


plt.figure(figsize=(8,5))
plt.scatter(Y_test,Y_pred, color ='blue', label = 'Predicted points')
plt.plot(Y_test, Y_test, color='red', label='Perfect prediction line')
plt.xlabel("Actual sale")
plt.ylabel("Predicted sales")
plt.title("Actual sales VS Predicted sales")
plt.legend()
plt.grid(True)
plt.show() 
