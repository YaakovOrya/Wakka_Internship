## Instructions for Reading CSV File into DataFrame

1. **Import Required Libraries**: Import the necessary library for data manipulation and visualization:

    ```python
    import pandas as pd
    ```

2. **Specify File Path**: Define the file path to your CSV file:

    ```python
    file_path = "/Users/yaakovhaiby/Desktop/WakkaInternship/DeepLearnigCourse/LogisticReg/logreg_data.csv"
    ```

3. **Read CSV File into DataFrame**: Use `pd.read_csv()` to read the CSV file into a pandas DataFrame, providing the file path:

    ```python
    df = pd.read_csv(file_path)
    ```

4. **Display DataFrame**: Use the `head()` function to display the first 5 rows of the DataFrame `df` and the `shape` attribute to display the dimensions of the DataFrame:

    ```python
    print(df.head())
    print(df.shape)
    ```

5. **Run the Code**: Execute the code in your Python environment to read the CSV file into a DataFrame.

6. **Troubleshooting**: If you encounter any errors or issues, refer to error messages and consult relevant documentation or resources for assistance.


