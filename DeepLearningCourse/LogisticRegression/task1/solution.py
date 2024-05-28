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


