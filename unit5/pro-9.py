import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="college")
cur = con.cursor()

columns = [
("name","varchar",20),
("qualification","varchar",20),
("post","varchar",20),
("salary","int",6)
]

sql = "create table employee("

for c in columns:
    sql += c[0] + " " + c[1] + "(" + str(c[2]) + "),"

sql = sql[:-1] + ")"

cur.execute(sql)

print("Table created")

con.close()
