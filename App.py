import mysql.connector
from tkinter import *
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    username="root",
    password="root",
    database="python_crud"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE python_crud")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
    # print(x)

# mycursor.execute("CREATE TABLE estudent (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), email VARCHAR(255))")

# mycursor.execute("DESC estudent")
# for x in mycursor:
    # print(x)

# sql = "INSERT INTO estudent (name,address,email) VALUES (%s,%s,%s)"
"""
val = [
    ("Angelina Pinto","Hera","angelinapint@gmail.com"),
    ("Alexandra Perreira","Pante Kelapa","alexandraper@gmail.com"),
    ("Basilio Mendonca","Lahane","basiliomendonca@gmail.com"),
    ("Donacio da Cruz","Becora","donaciodacr@gmail.com"),
    ("Elia Amaral","Hudi Laran","eliamaral@gmail.com")
]
"""

 #mycursor.executemany(sql,val)

# db.commit()

# print(mycursor.rowcount, "record(s) inserted!")

mycursor.execute("SELECT * FROM estudent")

result = mycursor.fetchall()

for x in result:
    print(x)

# template
class App(Frame):
    # constructor __init__
    # call superclass
    def __init__(self,master=None):
        super().__init__(master)
        self.master.iconbitmap("icon.ico")
        self.master.title("Haksolok Database")
        self.master.geometry("800x600")
        self.pack()
        # call method here
        self.all_here()

    # create a method
    def all_here(self):
        Heading = Label(self, text="Dadus Formandu", font=("ApercuMono.ttf",32))
        Heading.pack()


root = Tk()
crud = App(master=root)
root.mainloop()
