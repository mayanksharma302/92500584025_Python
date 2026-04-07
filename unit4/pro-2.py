import pandas as pd

df = pd.read_csv("students.csv")

print("Students from Rajkot City")
print(df[df["City"]=="Rajkot"])

print("Male Students")
print(df[df["Gender"]=="Male"])

print("Male Students from Rajkot City")
print(df[(df["Gender"]=="Male") & (df["City"]=="Rajkot")])

print("Students Age >= 20")
print(df[df["Age"]>=20])
