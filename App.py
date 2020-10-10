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

        create_button = Button(self, text="Create Date", bg="red", fg="white", font=("ApercuMono.ttf",10), command=self.create_window)
        create_button.pack(pady=10)

        read_button = Button(self, text="Read Date", bg="green", fg="white", font=("ApercuMono.ttf",10), command=self.read_window)
        read_button.pack(pady=10)

        update_button = Button(self, text="Update Date", bg="orange", fg="white", font=("ApercuMono.ttf",10), command=self.update_window)
        update_button.pack(pady=10)

        delete_button = Button(self, text="Delete Date", bg="chocolate", fg="white", font=("ApercuMono.ttf",10), command=self.delete_window)
        delete_button.pack(pady=10)

    # create date window
    def create_window(self):
        self.insert = Toplevel(self)
        self.insert.iconbitmap("icon.ico")
        self.insert.title("Insert Date")
        self.insert.geometry("400x300")

        insert_frame = Frame(self.insert)
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

    # read date window
    def read_window(self):
        read = Toplevel(self)
        read.iconbitmap("icon.ico")
        read.title("Read Date")
        read.geometry("600x400")

        mycursor.execute("SELECT * FROM estudent ORDER BY name ASC")
        result = mycursor.fetchall()

        form_index_frame = Frame(read)
        form_index_frame.pack()

        ApercuMono = ("ApercuMono.ttf",16)

        no = Label(form_index_frame, text="N0", font=ApercuMono)
        no.grid(row=0, column=0)

        name = Label(form_index_frame, text="Name", font=ApercuMono)
        name.grid(row=0, column=1, columnspan=4)

        address = Label(form_index_frame, text="Address", font=ApercuMono)
        address.grid(row=0, column=5, columnspan=4)

        email = Label(form_index_frame, text="Email", font=ApercuMono)
        email.grid(row=0, column=9, columnspan=4)

        ApercuMono = ("ApercuMono.ttf",13)

        for i,x in zip(range(1,len(result) + 1),result):
            no_estudent = Label(form_index_frame, text=f"{i}", font=ApercuMono)
            no_estudent.grid(row=i, column=0)

            name_estudent = Label(form_index_frame, text=f"{x[1]}", font=ApercuMono, anchor=W, justify=LEFT)
            name_estudent.grid(row=i, column=1, columnspan=4)

            address_estudent = Label(form_index_frame, text=f"{x[2]}", font=ApercuMono, anchor=W, justify=LEFT)
            address_estudent.grid(row=i, column=5, columnspan=4)

            email_estudent = Label(form_index_frame, text=f"{x[3]}", font=ApercuMono, anchor=W, justify=LEFT)
            email_estudent.grid(row=i, column=9, columnspan=4)

    # update date window
    def update_window(self):
        self.update = Toplevel()
        self.update.iconbitmap("icon.ico")
        self.update.title("Update Date")
        self.update.geometry("400x200")

        self.var = StringVar()
        self.var.set(None)

        sql = "SELECT name FROM estudent"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        a = []
        for x in result:
            for y in x:
                a.append(y)

        option = OptionMenu(self.update, self.var,*a)
        option.pack()

        confirm_button = Button(self.update, text="update", bg="orange", fg="white", command=self.to_update)
        confirm_button.pack(pady=20)

    def to_update(self):
        self.var.get()
        result = self.var.get()
        sql = "SELECT * FROM estudent WHERE name = %s"
        val = (result,)
        mycursor.execute(sql,val)
        result = mycursor.fetchall()
        x = []
        for i in result:
            for a in i:
                x.append(a)

        self.toupdate = Toplevel(self)
        self.toupdate.iconbitmap("icon.ico")
        self.toupdate.title("Update Date")
        self.toupdate.geometry("400x300")

        toupdate_frame = Frame(self.toupdate)
        toupdate_frame.pack()

        heading_toupdate = Label(toupdate_frame, text="Insert Date", font=("ApercuMono.ttf",20))
        heading_toupdate.grid(row=0, columnspan=2, pady=10)

        label_name = Label(toupdate_frame, text="Name:")
        label_name.grid(row=1, column=0, pady=4)
        self.toupdate_name = Entry(toupdate_frame)
        self.toupdate_name.grid(row=1, column=1, pady=4)
        self.toupdate_name.insert(0, x[1])

        label_address = Label(toupdate_frame, text="Address:")
        label_address.grid(row=2, column=0, pady=4)
        self.toupdate_address = Entry(toupdate_frame)
        self.toupdate_address.grid(row=2, column=1, pady=4)
        self.toupdate_address.insert(0, x[2])

        label_email = Label(toupdate_frame, text="Email:")
        label_email.grid(row=3, column=0, pady=4)
        self.toupdate_email = Entry(toupdate_frame)
        self.toupdate_email.grid(row=3, column=1, pady=4)
        self.toupdate_email.insert(0, x[3])

        toupdate_button = Button(toupdate_frame, text="OK", bg="blue", fg="white", font=("ApercuMono.ttf",12), command=self.query_toupdate)
        toupdate_button.grid(row=4, columnspan=2)

    # delete date window
    def delete_window(self):
        self.delete = Toplevel()
        self.delete.iconbitmap("icon.ico")
        self.delete.title("Delete Date")
        self.delete.geometry("400x200")

        self.var = StringVar()
        self.var.set(None)

        sql = "SELECT name FROM estudent"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        a = []
        for x in result:
            for y in x:
                a.append(y)

        option = OptionMenu(self.delete, self.var,*a)
        option.pack()

        confirm_button = Button(self.delete, text="deleted", bg="red", fg="white", command=self.query_delete)
        confirm_button.pack(pady=20)

    # query to create date
    def query_insert(self):
        # get all date in entry widget
        self.insert_name.focus_set()
        self.insert_address.focus_set()
        self.insert_email.focus_set()

        # include in variable
        name = self.insert_name.get()
        address = self.insert_address.get()
        email = self.insert_email.get()

        sql = "INSERT INTO estudent (name,address,email) VALUES (%s,%s,%s)"
        val = (name.capitalize(),address.capitalize(),email.lower())

        mycursor.execute(sql,val)

        db.commit()

        if( mycursor.rowcount > 0 ):
            messagebox.showinfo("success",f"{mycursor.rowcount} record(s) inserted!")
            self.insert_name.delete(0,END)
            self.insert_address.delete(0,END)
            self.insert_email.delete(0,END)
            self.insert.destroy()
        else:
            messagebox.showerror(f"{mycursor.rowcount} record(s) not inserted!")
            self.insert_name.delete(0,END)
            self.insert_address.delete(0,END)
            self.insert_email.delete(0,END)

    # query to update date
    def query_toupdate(self):
        self.toupdate_name.focus_set()
        self.toupdate_address.focus_set()
        self.toupdate_email.focus_set()

        name = self.toupdate_name.get()
        address = self.toupdate_address.get()
        email = self.toupdate_email.get()
        result = self.var.get()

        sql = "UPDATE estudent SET name = %s, address = %s, email = %s WHERE name = %s"
        val = (name.capitalize(),address.capitalize(),email.lower(),result)
        mycursor.execute(sql,val)

        db.commit()

        if( mycursor.rowcount > 0 ):
            messagebox.showinfo("success",f"{mycursor.rowcount} record(s) updated!")
        else:
            messagebox.showerror("faill",f"{mycursor.rowcount} record(s) not updated!")

    # query to delete date
    def query_delete(self):
        if( messagebox.askyesno("confirm",f"do you want to delete?") ):
            result = self.var.get()
            sql = "DELETE FROM estudent WHERE name = %s"
            val = (result,)
            mycursor.execute(sql,val)

            db.commit()

            if( mycursor.rowcount > 0 ):
                messagebox.showinfo("success",f"{mycursor.rowcount} record(s) deleted!")
                self.delete.destroy()
            else:
                messagebox.showwarning("faill",f"{mycursor.rowcount} record(s) not deleted!")
                self.delete.destroy()
        else:
            messagebox.showinfo("canceled","it's canceled to delete!")
            self.delete.destroy()


root = Tk()
crud = App(master=root)
root.mainloop()
