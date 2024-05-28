# Task: Plot the Data

1. **Import matplotlib.pyplot**: This library is used for data visualization. 
    ```python
     import matplotlib.pyplot as plt
    ```

2. **Create Scatter Plot**: Use matplotlib to create a scatter plot of the data. Specify the x and y variables, set labels for the x-axis and y-axis, add a title to the plot, and enable grid lines for better visualization.

    ```python

    plt.scatter(x, y)
    plt.xlabel("YearsExperience")
    plt.ylabel('Salary')
    plt.title("Scatter plot: YearsExperience vs Salary")
    plt.grid(True)
    plt.show()
    ```

3. **Run the Code**: Execute the code in your Python environment to generate the scatter plot.

4. **Troubleshooting**: If you encounter any errors or issues, refer to error messages and consult relevant documentation or resources for assistance.
