# omid_khosusi

import mysql.connector as mysql



db = mysql.connect(
    host = "localhost",
    user = "yuor user",
     password="your password",
     database = "your database"
)

cursor = db.cursor()

cursor.execute("SHOW TABLES")

tables = cursor.fetchall()

for table in tables:
    print(table)
