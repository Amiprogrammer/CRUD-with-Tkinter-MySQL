import mysql.connector
from tkinter import *
from tkinter import messagebox

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
