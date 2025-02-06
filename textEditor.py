import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, tk.END)

def saveFile():
    global filename
    t = text.get(0.0, tk.END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, tk.END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!", message="Unable to save file...")

def openFile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = tk.Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = tk.Text(root, width=400,height=400)
text.pack()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()