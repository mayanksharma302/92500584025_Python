import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

gender_count = df["Gender"].value_counts()

plt.bar(gender_count.index, gender_count.values)

plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.title("Male and Female Students")

plt.show()
