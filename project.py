from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="hospital", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()

#create function thats pulls all data from Login table in the hospital database
def verify():
    user_verification= Username.get()
    pass_verification = password.get()
    sql = "select * from Login where username = %s and password = %s"
    mycursor.execute(sql,[(user_verification), (pass_verification)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
            failed()

def logged():
    messagebox.showinfo("Login successful", "Verified!")


def failed():
    messagebox.showerror("Login failed", "Please check your username and password.")


root.title('Login Page')

root.geometry("450x450")
root.configure(background="black")


lbluser=tk.Label(root, text="Enter Username")
lbluser.place(x=50, y=20)

Username= tk.Entry(root, width=30)
Username.place(x=165,y=20)

lblpasswd=tk.Label(root,text="Enter Password")
lblpasswd.place(x=50, y=60)

password = tk.Entry(root,width=30)
password.place(x=165, y=60)

logbuttn=tk.Button(root,text="Login", command=verify)
logbuttn.place(x=145,y=100)

regbuttn=tk.Button(root,text="Register")
regbuttn.place(x=220,y=100)









root.mainloop()
