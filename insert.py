import mysql.connector

mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="hospital", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()

sql = "INSERT INTO Login (username, password) VALUES (%s, %s)"
val = ("Godwin", "12345")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
