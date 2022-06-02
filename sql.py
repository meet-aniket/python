import mysql.connector

myDB = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NINJA420",
  database="testDB"
)

myCursor = myDB.cursor();

# myCursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

myCursor.execute("SHOW TABLES")

for x in myCursor:
  print(x);