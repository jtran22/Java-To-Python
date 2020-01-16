# currently has a pull GUI to get the file path of the file the user wants to
# translate
import tkinter as tk
from tkinter import filedialog
from tkinter import *

file_path = "None Selected"
base = tk.Tk()
base.title("Java to Python translator.")


def execute_items():
    print("Blah")


def set_file_path(path):
    global file_path
    file_path = path
    if not check_valid():
        popupmsg("Invalid filetype, must be .java")
    else:
        fl = Label(base, text="Current File: {}".format(file_path))
        fl.pack()
        execute_items()


def check_valid():
    global file_path
    if(file_path.find(".java", len(file_path)-5, len(file_path)) != -1 or
            file_path == "None Selected"):
        return True
    else:
        return False


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Invalid")
    label = Label(popup, text=msg)
    label.pack()
    b2 = tk.Button(popup, text="Okay", command=popup.destroy)
    b2.pack()
    popup.mainloop()


b = tk.Button(base, text="Select '.java' file", width=50,
              command=lambda *args: set_file_path(filedialog.askopenfilename()
                                                  ))
b.pack()

base.mainloop()
