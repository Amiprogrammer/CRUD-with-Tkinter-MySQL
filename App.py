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
        Heading.pack(pady=30)

        insert_button = Button(self, text="Insert Date", bg="red", fg="white", font=("ApercuMono.ttf",10), command=self.insert_date)
        insert_button.pack(pady=10)

        # call read_date method here
        self.read_date()

    def read_date(self):
        mycursor.execute("SELECT * FROM estudent")
        result = mycursor.fetchall()

        form_index_frame = Frame(self)
        form_index_frame.pack()

        ApercuMono = ("ApercuMono.ttf",16)

        no = Label(form_index_frame, text="N0", font=ApercuMono)
        no.grid(row=0, column=0)

        name = Label(form_index_frame, text="Name", font=ApercuMono)
        name.grid(row=0, column=1, columnspan=4)

        address = Label(form_index_frame, text="Address", font=ApercuMono)
        address.grid(row=0, column=5, columnspan=4)

        email = Label(form_index_frame, text="email", font=ApercuMono)
        email.grid(row=0, column=9, columnspan=4)

        ApercuMono = ("ApercuMono.ttf",13)

        for i,x in zip(range(1,len(result) + 1),result):
            no_estudent = Label(form_index_frame, text=f"{x[0]}", font=ApercuMono)
            no_estudent.grid(row=i, column=0)

            name_estudent = Label(form_index_frame, text=f"{x[1]}", font=ApercuMono, anchor=W, justify=LEFT)
            name_estudent.grid(row=i, column=1, columnspan=4)

            address_estudent = Label(form_index_frame, text=f"{x[2]}", font=ApercuMono, anchor=W, justify=LEFT)
            address_estudent.grid(row=i, column=5, columnspan=4)

            email_estudent = Label(form_index_frame, text=f"{x[3]}", font=ApercuMono, anchor=W, justify=LEFT)
            email_estudent.grid(row=i, column=9, columnspan=4)

    def insert_date(self):
        top = Toplevel(self)
        top.iconbitmap("icon.ico")
        top.title("Insert Date")
        top.geometry("400x300")

        insert_frame = Frame(top)
        insert_frame.pack()

        heading_insert = Label(insert_frame, text="Insert Date", font=("ApercuMono.ttf",20))
        heading_insert.grid(row=0, columnspan=2, pady=10)

        label_name = Label(insert_frame, text="Name:")
        label_name.grid(row=1, column=0, pady=4)
        self.insert_name = Entry(insert_frame)
        self.insert_name.grid(row=1, column=1, pady=4)

        label_address = Label(insert_frame, text="Address:")
        label_address.grid(row=2, column=0, pady=4)
        self.insert_address = Entry(insert_frame)
        self.insert_address.grid(row=2, column=1, pady=4)

        label_email = Label(insert_frame, text="Email:")
        label_email.grid(row=3, column=0, pady=4)
        self.insert_email = Entry(insert_frame)
        self.insert_email.grid(row=3, column=1, pady=4)

        insert_button = Button(insert_frame, text="OK", bg="blue", fg="white", font=("ApercuMono.ttf",12), command=self.query_insert)
        insert_button.grid(row=4, columnspan=2)

    def query_insert(self):
        # get all date in entry widget
        self.insert_name.focus_set()
        self.insert_address.focus_set()
        self.insert_email.focus_set()

        # include in variable
        name = self.insert_name.get()
        address = self.insert_address.get()
        email = self.insert_email.get()
        # convert to capitalize & lowercase letter
        name.capitalize()
        address.capitalize()
        email.lower()

        sql = "INSERT INTO estudent (name,address,email) VALUES (%s,%s,%s)"
        val = (name,address,email)

        mycursor.execute(sql,val)

        db.commit()

        if( mycursor.rowcount > 0 ):
            messagebox.showinfo("success",f"{mycursor.rowcount} record(s) inserted!")
            self.insert_name.delete(0,END)
            self.insert_address.delete(0,END)
            self.insert_email.delete(0,END)
        else:
            messagebox.showerror(f"{mycursor.rowcount} record(s) not inserted!")
            self.insert_name.delete(0,END)
            self.insert_address.delete(0,END)
            self.insert_email.delete(0,END)


root = Tk()
crud = App(master=root)
root.mainloop()
