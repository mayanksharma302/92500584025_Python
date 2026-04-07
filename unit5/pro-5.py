import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")

cur = con.cursor()

roll = int(input("Enter Roll No to update: "))
city = input("Enter New City: ")

sql = "update student set City=%s where RollNo=%s"

cur.execute(sql,(city,roll))

con.commit()

print("Record updated")

con.close()
