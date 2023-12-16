from tkinter import *

root = Tk()

root.title("first page")
root.geometry("500x500")
root.resizable(1, 0)

def newTab():
    window = Tk()

    window.title("first page")
    window.geometry("500x500")
    window.resizable(1, 0)

lbl1 = Label(root, text="first name").place(x=10, y=10)
lbl2 = Label(root, text="first name").pack()
ent1 = Entry(root, width=50).pack()
btn = Button(root, text="submit", command=lambda : newTab()).pack()

root.mainloop() 