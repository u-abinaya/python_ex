

import pandas as pd

# Create Pandas Series
marks = pd.Series(
    [85, 91, 78, 88, 95],
    index=["A", "B", "C", "D", "E"]
)

print("--- Pandas Series ---")
print(marks)

# Create DataFrame
data = {
    "RollNo": [101, 102, 103, 104, 105],
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
    "Mark": [85, 91, 78, 88, 95]
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

# Calculate average mark
print("\nAverage Mark:", round(df["Mark"].mean(), 2))

# Display students scoring above 85