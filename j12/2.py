from tkinter import *

root = Tk()
root.title("fullname")
root.geometry("500x500")
root.resizable(0, 0)

f_lbl = Label(root, text="firstname", font=("Arial", 20), fg="black").place(x=10, y=10)
f_ent = Entry(root, font=("Arial", 20), bd=5).place(x=150, y=15)
l_lbl = Label(root, text="lastname", font=("Arial", 20), fg="black").place(x=10, y=70)
L_ent = Entry(root, font=("Arial", 20), bd=5).place(x=150, y=65)



root.mainloop()