import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")

cur = con.cursor()

roll = int(input("Enter Roll No: "))

cur.execute("select * from student where RollNo=%s",(roll,))

row = cur.fetchone()

if row:
    print(row)
else:
    print("Student not found")

con.close()
