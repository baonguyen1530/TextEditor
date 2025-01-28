import Tkinter import *
import tFileDialog import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)