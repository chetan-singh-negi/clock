from tkinter import *
from time import strftime
def samay():
    current=strftime('%H:%M:%S %p')
    print(current)
    L.config(text=current)
    L.after(1000,samay)
root=Tk()
root.geometry("600x200")
root.title("clock")
f=Frame(root,bg="yellow",width=550,height=150)
f.pack()
L=Label(f,fg="black",font="lucida 70 bold")
L.pack(padx=20,pady=20)
samay()
root.mainloop()
