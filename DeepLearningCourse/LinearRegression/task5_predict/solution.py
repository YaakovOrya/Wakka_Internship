
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np


file_path = "/Users/yaakovhaiby/Desktop/yaakov-haiby-wakka-internship/DeepLearningCourse/LinearRegression/Salary_Data.csv"
#col_names = ["x", "y"]
#df = pd.read_csv(file_path, names=col_names)

data = {
    "x": [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6.0, 6.8, 7.1, 7.9, 8.2, 8.7, 9.0, 9.5, 9.6, 10.3, 10.5],
    "y": [39343.00, 46205.00, 37731.00, 43525.00, 39891.00, 56642.00, 60150.00, 54445.00, 64445.00, 57189.00, 63218.00, 55794.00, 56957.00, 57081.00, 61111.00, 67938.00, 66029.00, 83088.00, 81363.00, 93940.00, 91738.00, 98273.00, 101302.00, 113812.00, 109431.00, 105582.00, 116969.00, 112635.00, 122391.00, 121872.00]
}

df = pd.DataFrame(data)

print(df.shape)

print(df.head(5))



x = df['x']
y = df['y']




plt.scatter(x, y)
plt.xlabel("YearsExperience")
plt.ylabel('Salary')
plt.title("Scatter plot: YearsExperience vs Salary")
plt.grid(True)
plt.show()


x_values = x.values.reshape(-1, 1)
model = LinearRegression()
model.fit(x_values, y)

slope = model.coef_[0]
intercept = model.intercept_

plt.scatter(x, y)

plt.plot(x, slope * x + intercept, color='red')
plt.xlabel("YearsExperience")
plt.ylabel('Salary')
plt.title("Scatter plot with Regression Line: YearsExperience vs Salary")
plt.grid(True)
plt.show()

years_input = float(input("Enter the number of years of experience:  "))
predicted_salary = model.predict(np.array([[years_input]]))
predicted_salary = predicted_salary[0].round(3)
print(f"Predicted salary for {years_input} years of experience is {predicted_salary} $")


