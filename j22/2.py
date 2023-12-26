import tkinter as tk
from tkinter import filedialog, colorchooser

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        text.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text.insert(tk.INSERT, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

def change_theme():
    if theme_var.get() == "Dark":
        root.configure(bg="#121212")
        text.configure(bg="#1e1e1e", fg="#ffffff")
        file.entryconfigure(0, command=new_file)
        file.entryconfigure(1, command=open_file)
        file.entryconfigure(2, command=save_file)
        view.entryconfigure(0, command=lambda: change_font_size(-1))
        view.entryconfigure(1, command=lambda: change_font_size(1))
        theme_var.set("Light")
    else:
        root.configure(bg="#ffffff")
        text.configure(bg="#ffffff", fg="#000000")
        file.entryconfigure(0, command=new_file)
        file.entryconfigure(1, command=open_file)
        file.entryconfigure(2, command=save_file)
        view.entryconfigure(0, command=lambda: change_font_size(-1))
        view.entryconfigure(1, command=lambda: change_font_size(1))
        theme_var.set("Dark")

def change_font_size(delta):
    current_font = text.cget("font")
    size = str(int(current_font.split(" ")[1]) + delta)
    new_font = (current_font.split(" ")[0], size)
    text.configure(font=new_font)

root = tk.Tk()
root.title("Notepad")

theme_var = tk.StringVar()
theme_var.set("Light")

text = tk.Text(root)
text.pack(expand=True, fill=tk.BOTH)

menu = tk.Menu(root)
root.config(menu=menu)

file = tk.Menu(menu)
menu.add_cascade(label="File", menu=file)
file.add_command(label="New", command=new_file)
file.add_command(label="Open", command=open_file)
file.add_command(label="Save", command=save_file)

view = tk.Menu(menu)
menu.add_cascade(label="View", menu=view)
view.add_command(label="Dark Mode", command=change_theme)
view.add_command(label="Increase Font Size", command=lambda: change_font_size(1))
view.add_command(label="Decrease Font Size", command=lambda: change_font_size(-1))

root.mainloop()