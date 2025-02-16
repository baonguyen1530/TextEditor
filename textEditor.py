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
    if filename:
        t = text.get(0.0, tk.END)
        try:
            with open(filename, 'w') as f:
                f.write(t)  
        except:           
            messagebox.showerror(title="Oops!", message="Unable to save file...")
    else:
        saveAs()    #if no filename, prompt for saveAs

def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if f:
        t = text.get(0.0, tk.END)
        try:
            f.write(t.rstrip())
            global filename
            filename = f.name   #update the filename
        except:
            messagebox.showerror(title="Oops!", message="Unable to save file...")

def openFile():
    f = filedialog.askopenfile(mode='r')
    if f:       #check if a file was selected
        t = f.read()
        text.delete(0.0, tk.END)
        text.insert(0.0, t)
        global filename
        filename = f.name
        f.close()

root = tk.Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = tk.Text(root, width=400,height=400)
text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

'''
A status bar can display useful information, such as:
 -the current file name
 -the cursor position (line & column)
 -word or character count
'''
status = tk.Label(root, text="Line: 1 | Column: 1", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

def update_status_bar(event=None):
    line, column = text.index(tk.INSERT).split('.')
    status.config(text=f"Line: {line} | Column: {column}")

text.bind("<KeyRelease>", update_status_bar)
text.bind("<ButtonRelease>", update_status_bar)

#Menu bar
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