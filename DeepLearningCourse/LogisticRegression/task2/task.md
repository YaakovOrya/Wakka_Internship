## Splitting Data into Features and Target Variable

When working with machine learning models, it's common to split your dataset into features (inputs) and the target variable (output).
```python
# Splitting the data into features and target variable
X = df[['x']]  # Feature 'x' (using double square brackets to ensure X is a DataFrame Matrix)
y = df['y']    # Target 'y'
 ```