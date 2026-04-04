import numpy as np

X = [1,2,3,4,5]
Y = [3,4,2,4,5]

#mean X
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

slope = Numerator / Denominator

print("Slope od the line : ",slope)

#intercept

c = meanY - slope * meanX

print("Intercept : ",c)

#PREDICT Y FOR X = 6
X = 6

Y = 0.4 * (X) + 2.4

print("predicted Y for X = 6 ",Y)


