import tkinter as tk
from tkinter import ttk


raiz = tk.Tk()
raiz.title("hola")
raiz.geometry("1000x850")
raiz.config(bg ="gray")
raiz.config(bd="30")
raiz.config(relief="groove")

miframe = tk.Frame(raiz, bg="white", width="1000", height="650")
miframe.pack(fill="both", expand="True")



import calendar
m=calendar.Calendar()

dias=list()
diasdelaño=list()

for x in range(13):
    if x==0:
        pass
    else:
        m=calendar.monthcalendar(2023,x)

        for a in m:
            for b in a:
                if b==0:
                    pass
                else:
                    c=str(b)
                    dias.append(c)
            
print(dias)
print(len(dias))