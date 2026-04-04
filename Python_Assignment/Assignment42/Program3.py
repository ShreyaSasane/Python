from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Training data
Experience = [[1],[2],[3],[4],[5]]
Salary = [20000, 25000, 30000,35000,40000]

# Train model
model = LinearRegression()
model.fit(Experience, Salary)

# Predict for new value
new_exp = [[6]]
y_pred = model.predict(new_exp)
print(y_pred)

# Regression line predictions for training data
line_pred = model.predict(Experience)

# Plot
plt.scatter(Experience, Salary, color='blue', label='Actual Salary')
plt.plot(Experience, line_pred, color='red', label='Regression Line')

# Plot predicted point
plt.scatter(new_exp, y_pred, color='green', label='Predicted Salary (6 yrs)')

plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience VS Salary Regression line")
plt.legend()
plt.grid(True)
plt.show()