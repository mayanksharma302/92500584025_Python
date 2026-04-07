import pandas as pd
import re

df = pd.read_csv("students.csv")

pattern = r'^\d{2}-\d{10}$'

valid_mobile = df[df["Mobile"].str.match(pattern)]

print(valid_mobile)
