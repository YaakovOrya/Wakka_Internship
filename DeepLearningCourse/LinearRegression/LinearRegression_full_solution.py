from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task: Import the data
file_path = "/Users/yaakovhaiby/Desktop/WakkaInternship/DeepLearnigCourse/linearReg/Salary_Data.csv"
col_names = ["x", "y"]
df = pd.read_csv(file_path, names=col_names)
# x is the years_of_experience variable , and y is the employee's salary  





# Data cleaning(by us)

df = df.drop(index=0)
df['y'] = pd.to_numeric(df['y'], errors='coerce')  # Convert 'y' column to numeric

df['x'] = df['x'].astype(float)
df['y'] = df['y'].round(2)

x = df['x']
y = df['y']



# Task: show a small part of the data
print(df.head(5))



# Task: plot the data 

plt.scatter(x, y,)
plt.xlabel("YearsExperience")
plt.ylabel('Salary')
plt.title("Scatter plot: YearsExperience vs Salary")
plt.grid(True)
plt.show()





# Task: Fit a linear regression model and plot the data with the regression line

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



# Task: What is the predicted salary for the user's input?

years_input = float(input("Enter the number of years of experience:  "))
predicted_salary = model.predict(np.array([[years_input]]))
predicted_salary = predicted_salary[0].round(3)
print(f"Predicted salary for {years_input} years of experience is {predicted_salary} $")






