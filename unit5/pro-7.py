import mysql.connector
import re

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")
cur = con.cursor()

cur.execute("select * from student")

rows = cur.fetchall()

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

for r in rows:
    if re.match(pattern, r[5]):
        print(r)

con.close()
