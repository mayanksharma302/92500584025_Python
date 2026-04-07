import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")
cur = con.cursor()

cur.execute("select * from student where Name like 'N____'")

rows = cur.fetchall()

for r in rows:
    print(r)

con.close()
