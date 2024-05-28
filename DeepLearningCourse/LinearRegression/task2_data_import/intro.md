## Let's start with the data!

Any good analyis starts with data.

In this task, we will be giving you data that contains salaries and years of experience. We will be using this data to fit a linear regression model.

The first step is to import the data. For that, we will be using the pandas library. To use the pandas library, we will be using the following code:

```python
import pandas as pd
```

That code imports the pandas library and creates a short alias for it called `pd`.

### Printing the dimentions of the data

To print the dimensions of the DataFrame `df`, use the `shape` attribute.

```python
print(df.shape)
```

This prints a tuple representing the dimensions of the DataFrame, where the first element is the number of rows and the second element is the number of columns.


### Print DataFrame Head

To display the first few rows of the DataFrame `df`, we use the following code:

```python
print(df.head(5))
```

Explanation of the code:
- **`df`**: Refers to the DataFrame containing the data.
- **`.head(5)`**: Calls the `head()` method on the DataFrame, specifying that we want to retrieve the first 5 rows.
- **`print(df.head(5))`**: Prints the first 5 rows of the DataFrame to the console.

Displaying a small part of the data allows us to quickly inspect the structure and content of the DataFrame. It provides a snapshot of the data, including column names and sample values, which can be useful for initial exploration and understanding of the dataset.
