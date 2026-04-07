import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")

cur = con.cursor()

roll = int(input("Enter Roll No: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
city = input("Enter City: ")

sql = "insert into student values(%s,%s,%s,%s,%s)"

cur.execute(sql,(roll,name,age,gender,city))

con.commit()

print("Record inserted")

con.close()
