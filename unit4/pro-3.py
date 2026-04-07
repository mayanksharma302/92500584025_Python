import pandas as pd

df = pd.read_csv("students.csv")

print("Original Data")
print(df)

print("After dropna()")
print(df.dropna())

print("After fillna()")
print(df.fillna("Not Available"))
