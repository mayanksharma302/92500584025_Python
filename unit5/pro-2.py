import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")

cur = con.cursor()

cur.execute("select * from student")

rows = cur.fetchall()

for r in rows:
    print(r)

con.close()
