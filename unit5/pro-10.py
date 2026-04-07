import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")
cur = con.cursor()

while True:

    print("1 Insert Student")
    print("2 Update Student")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 List Students")
    print("6 Exit")

    ch = int(input("Enter choice: "))

    if ch==1:
        roll = int(input("Roll No: "))
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        city = input("City: ")

        cur.execute("insert into student values(%s,%s,%s,%s,%s)",(roll,name,age,gender,city))
        con.commit()
        print("Inserted")

    elif ch==2:
        roll = int(input("Roll No: "))
        city = input("New City: ")

        cur.execute("update student set City=%s where RollNo=%s",(city,roll))
        con.commit()
        print("Updated")

    elif ch==3:
        roll = int(input("Roll No: "))
        cur.execute("select * from student where RollNo=%s",(roll,))
        row = cur.fetchone()

        if row:
            print(row)
        else:
            print("Student not found")

    elif ch==4:
        roll = int(input("Roll No: "))
        cur.execute("delete from student where RollNo=%s",(roll,))
        con.commit()
        print("Deleted")

    elif ch==5:
        cur.execute("select * from student")
        rows = cur.fetchall()

        for r in rows:
            print(r)

    elif ch==6:
        break

con.close()
