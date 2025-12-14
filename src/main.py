import pandas as pd
import numpy as np

# 1️⃣ Create a DataFrame using NumPy and Pandas
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
ages = np.array([25, 30, 35, 40, 28])
scores = np.array([85, 90, 95, 80, 88])

df = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "Score": scores
})

print("Original DataFrame:\n", df)

# 2️⃣ Basic DataFrame info and statistics
print("\nDataFrame Info:")
print(df.info())

print("\nDataFrame Description:")
print(df.describe())

# 3️⃣ Selecting columns
print("\nSelecting 'Name' and 'Score':")
print(df[['Name', 'Score']])

# 4️⃣ Filtering rows using NumPy conditions
print("\nPeople with Score > 85:")
print(df[np.array(df['Score'] > 85)])

# 5️⃣ Adding a new column using NumPy
df['Passed'] = np.where(df['Score'] >= 85, True, False)
print("\nDataFrame after adding 'Passed' column:\n", df)

# 6️⃣ Modifying existing column using NumPy
df['Score'] = df['Score'] + 5
print("\nDataFrame after increasing scores by 5:\n", df)

# 7️⃣ Sorting DataFrame
print("\nDataFrame sorted by Age:")
print(df.sort_values(by='Age'))

# 8️⃣ Using NumPy to calculate mean score
mean_score = np.mean(df['Score'])
print("\nMean Score:", mean_score)
