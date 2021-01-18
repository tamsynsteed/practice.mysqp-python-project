import mysql.connector
mydb=mysql.connector.connect(user="tamsynsteed", passwd="@Lifechoices314", database="hospital", host="127.0.0.1", auth_plugin="mysql_native_password")
mycurscor=mydb.cursor()
mycurscor.execute("Select * from Dentists")
for x in mycurscor:
    print(x)
