import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox
class Passwordgen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(width=300,height=400)
        self.resizable(False,False)
        self.title("Rpg")
        toplbl=tk.Label(self,text="Random password generator",
                        fg="white",
                        bg="skyblue",
                        height=2,
                        font=("poppins",11))
        toplbl.place(relwidth=1,y=0)
        passwordlbl=tk.Label(self,height=3,bg="white")
        passwordlbl.place(relwidth=0.99,y=50)
        def evaluate():
            x=leh.get()
            if x !="":
                 lenght=int(x)
                 chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678!£$%^&*()_"
                 password="".join(random.sample(chars,lenght))
                 passwordlbl.config(text=password)
            else:
                messagebox.showerror("pg","Please enter the lenght of the password")
        lehlbl=tk.Label(self,text="Enter the length of the password",font=("poppins",11))
        lehlbl.place(relwidth=0.9,y=170)
        leh=tk.Entry(self,)
        leh.place(x=90,y=210)
        btn=tk.Button(self,text="generate password",height=2,
                            bg="skyblue",fg="white",
                            command=evaluate
                            )
        btn.place(x=95,y=300)
        devlbl=tk.Label(self,text="*******Developed by Mr john********",font=("candara",11),fg="grey")
        devlbl.place(relwidth=1,y=370)
       
if __name__=="__main__":
    app=Passwordgen()
    app.mainloop()