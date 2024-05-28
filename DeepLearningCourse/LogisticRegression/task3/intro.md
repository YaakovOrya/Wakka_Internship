## Explanation of Code

### Plotting the Data
1. **Importing matplotlib.pyplot as plt**: This line of code is used to import the `matplotlib.pyplot` module, which is a part of the `matplotlib` library. The `matplotlib.pyplot` module provides a MATLAB-like interface for creating plots and visualizations. It is commonly imported as `plt` for brevity and convenience.


This code snippet plots the data points without the logistic regression curve.

- **`plt.scatter(X, y, color='blue')`**: Plots the data points using a scatter plot, where X represents the feature and y represents the target variable.
- **`plt.xlabel('x')`**: Sets the label for the x-axis as 'x'.
- **`plt.ylabel('y')`**: Sets the label for the y-axis as 'y'.
- **`plt.title('Data')`**: Sets the title of the plot as 'Data'.
- **`plt.grid(True)`**: Displays grid lines on the plot.
- **`plt.show()`**: Renders the plot.

### Purpose

This code chunk visualizes the distribution of data points in the dataset, aiding in understanding the data's characteristics before model fitting.
