import mysql.connector as conn

mydb=conn.connect(host='localhost',user='root',passwd="Ja_va@123")

print(mydb)