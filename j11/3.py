from tkinter import *

root = Tk()
root.title("first application")
root.geometry("500x500")
root.resizable(False, False)
l = Label(root, text="First application", font=25,foreground="green").place(x=200, y=250)
root.mainloop()