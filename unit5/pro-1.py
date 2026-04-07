import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")

cur = con.cursor()

cur.execute("select * from student")

row = cur.fetchone()

while row is not None:
    print(row)
    row = cur.fetchone()

con.close()
