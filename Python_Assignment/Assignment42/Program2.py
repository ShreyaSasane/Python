import numpy as np

X = [1,2,3,4,5]
Y = [3,4,2,4,5]

numX = len(X)

meanX = sum(X) / numX

print("Mean of X :",meanX)

#mean Y
numY = len(Y)

meanY = sum(Y) / numY

print("Mean of Y",meanY)

#slope
Numerator = 0
Denominator = 0

for i in range(numX):
    Numerator += ((X[i] - meanX) * (Y[i] - meanY))
    Denominator += ((X[i] - meanX) ** 2)

m = Numerator / Denominator

print("Slope od the line : ",m)

#intercept

c = meanY - m * meanX

print("Intercept : ",c)

y_pred = []

for i in range(numX):
    y = X[i] * m + c
    y_pred.append(y)

print("Predicted all Y values : ", y_pred)

#mean Squared error 

mse = 0
error = 0

for i in range(numX):

    error = X[i] - Y[i]
    mse = mse + error ** 2


MSE = mse / numX

print("Mean Squared error : ",MSE)

#R2 Score

model_error = 0
for i in range(numX):
    model_error = model_error + (Y[i] - y_pred[i]) ** 2

mean_error = 0
for i in range(numX):
    mean_error += (Y[i] - meanY) ** 2

R2 = 1 - (model_error / mean_error)

print("R2 Score : ",R2 * 100)