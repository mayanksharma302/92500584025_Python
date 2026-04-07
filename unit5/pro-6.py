import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")
cur = con.cursor()

roll = int(input("Enter Roll No to delete: "))

sql = "delete from student where RollNo=%s"
cur.execute(sql,(roll,))

con.commit()

print("Record deleted")

con.close()
