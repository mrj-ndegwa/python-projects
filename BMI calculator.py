import tkinter as tk
from tkinter import messagebox
class myapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(width=400,height=400)
        self.resizable(False,False)
        self.title("my bmi calculator")
        dslbl=tk.Label(self,width=55,height="5",bg="black")
        dslbl.place(x=5,y=5)
        def calculate():
            h=displayh.get()
            m=displaym.get()
            if m=="" or h == "":
                messagebox.showerror("Bmi","Please enter some values")
            elif h!="" or m!="":
                xm=float(m)
                yh=float(h)
                inmeters=yh/100
                squared=inmeters*inmeters
                results=xm/squared
                r="your body mass index is:"+" "+str(results)
                display.config(text=r)
                if results < 18.5:
                    messagebox.showinfo("Bmi Analysis","You are underweight my friend")
                elif results > 18.5 and results < 25.0:
                    messagebox.showinfo("Bmi Analysis","You are healthy")
                elif(results > 25.0 and results < 30.0):
                    messagebox.showinfo("Bmi Analysis","You are overweight my friend")
                elif(results > 30.0):
                    messagebox.showwarning("Bmi Analysis","You are sick my friend")
            
        calc=tk.Button(self,text="Calculate",
                            width=15,
                            height=2,
                            bg="#14c714",
                            fg="white",
                            command=lambda:calculate())
        calc.place(x=140,y=250)
        display=tk.Label(dslbl,bg="white")
        display.place(relwidth=0.995,relheight=1)
        wlbl=tk.Label(self,width=20,height=3,bg="black")
        weightlbl=tk.Label(self,text="Mass(Kg)")
        weightlbl.place(x=10,y=120)
        heightlbl=tk.Label(self,text="Height(cm)")
        heightlbl.place(x=230,y=120)
        wlbl.place(x=10,y=150)
        mlbl=tk.Label(self,width=20,height=3,bg="black")
        mlbl.place(x=230,y=150)
        displaym=tk.Entry(wlbl)
        displaym.place(relwidth=0.995,relheight=1)
        displayh=tk.Entry(mlbl)
        displayh.place(relwidth=0.995,relheight=1)
        dev=tk.Label(self,text="********developed by mr john 2023*******",font=("candara","11"),fg="grey")
        dev.place(relwidth=1,y=360)
       
if __name__=="__main__":
    run=myapp()
    run.mainloop()
