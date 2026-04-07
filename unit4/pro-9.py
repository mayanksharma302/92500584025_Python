import pandas as pd
import re

df = pd.read_csv("students.csv")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

valid_email = df[df["Email"].str.match(pattern)]

print(valid_email)
