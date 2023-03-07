import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="GurraG2006"
)

print(mydb)