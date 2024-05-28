from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#file_path = "/Users/yaakovhaiby/Desktop/yaakov-haiby-wakka-internship/DeepLearningCourse/LogisticRegression/LogisticRegression_data.csv"
#df = pd.read_csv(file_path)

data = {
    "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "y": [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)


print(df.head())
print(df.shape)


X = df[['x']]  
y = df['y']    


plt.scatter(X, y, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data')
plt.grid(True)
plt.show()

model = LogisticRegression()
model.fit(X, y)

plt.scatter(X, y, color='blue', label='Data')
x_values = np.linspace(X.min(), X.max(), 100)
y_values = model.predict_proba(x_values.reshape(-1, 1))[:,1]
plt.plot(x_values, y_values, color='red', label='Logistic Regression')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Data with Logistic Regression Curve')
plt.legend()
plt.grid(True)
plt.show()