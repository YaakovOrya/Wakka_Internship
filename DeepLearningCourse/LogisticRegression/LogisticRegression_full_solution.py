import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression




#The goal of logistic regression is to model the probability that a given input belongs to a particular category or class. 
#It's commonly used for binary classification problems, where the target variable has two possible outcomes. 
#The model learns the relationship between the input features and the probability of belonging to one of the two classes, enabling predictions and inference based on new data.


# Task: load the data

file_path = "/Users/yaakovhaiby/Desktop/WakkaInternship/DeepLearnigCourse/LogisticReg/logreg_data.csv"
df = pd.read_csv(file_path)

# Task: show the data frame

print(df.head())



# Task: Split the data into features (X) and target variable (y)
X = df[['x']]  # Feature 'x'
y = df['y']    # Target 'y'



# Task: Plot the data without the logistic regression curve
plt.scatter(X, y, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data')
plt.grid(True)
plt.show()


# Task: Initialize the Logistic Regression model + Fit the model to the entire dataset + Plot the logistic regression curve


model = LogisticRegression()
model.fit(X, y)

plt.scatter(X, y, color='blue', label='Data')
x_values = np.linspace(X.min(), X.max(), 100)
y_values = model.predict_proba(x_values.reshape(-1, 1))[:,1]
plt.plot(x_values, y_values, color='red', label='Logistic Regression')

# This curve visually represents the relationship between the input feature and the probability of belonging to class 1.

plt.xlabel('x')
plt.ylabel('y')
plt.title('Data with Logistic Regression Curve')
plt.legend()
plt.grid(True)
plt.show()



# Task: Predict the class for x = 14.23

new_x = np.array([[14.23]])

predicted_class = model.predict(new_x)

print(f"The predicted class for x = {new_x[0][0]} is: {predicted_class[0]}")

