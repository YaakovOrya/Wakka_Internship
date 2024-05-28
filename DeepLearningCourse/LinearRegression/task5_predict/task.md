# Task: Predict Salary Based on User Input

1. **Import Libraries**: Import the `numpy` library.

    ```python
    import numpy as np
    ```

2. **Get User Input**: Prompt the user to enter the number of years of experience using the `input()` function and convert the input to a float value.

    ```python
    years_input = float(input("Enter the number of years of experience:  "))
    ```

3. **Make Prediction**: Use the fitted linear regression model (`model`) to predict the salary based on the user's input. Convert the input to a numpy array and reshape it to match the model's input requirements. Then, use the `predict()` method to obtain the predicted salary.

    ```python
    predicted_salary = model.predict(np.array([[years_input]]))
    ```

4. **Round Predicted Salary**: Round the predicted salary to a desired precision.

    ```python
    predicted_salary = predicted_salary[0].round(3)
    ```

5. **Display Prediction**: Print the predicted salary for the user's input using f-strings or string formatting.

    ```python
    print(f"Predicted salary for {years_input} years of experience is {predicted_salary} $")
    ```

6. **Run the Code**: Execute the code in your Python environment and enter the desired number of years of experience when prompted.

7. **Troubleshooting**: If you encounter any errors or issues, refer to error messages and consult relevant documentation or resources for assistance.
