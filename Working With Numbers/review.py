import tkinter as tk
from tkinter import ttk


class InvestmentFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)
    # Define string variable for the entry field
        self.monthlyInvestment = tk.StringVar()
    # Create a label, an entry field, and a button
        ttk.Label(self, text="Monthly Investment:").grid(column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.monthlyInvestment).grid(column=1, row=0)
        ttk.Button(self, text="Clear", command=self.clear).grid(column=2, row=0)
        # Add padding to all child components
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def clear(self):
        print("Monthly Investment:",
              self.monthlyInvestment.get())

        self.monthlyInvestment.set("")


if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    root.title("Future Value Calculator")
    InvestmentFrame(root)  # Create the frame
    root.mainloop()  # Display the frame


import tkinter as tk

window = tk.Tk()
window.title("Name")
window.geometry("300x150")

"""
The constructor of the root window
Tk()
The methods of the root window
title(title)
geometry(str)
mainloop()
"""

from tkinter import ttk
# How to add a frame to the root window
frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

"""
Two constructors of the ttk module
Frame(parent[, padding])
Button(parent, text)
A method for working with all components
pack([fill][, expand])
"""

# How to add two buttons to the frame
button1 = ttk.Button(frame, text="Click me",
command=click_button1)
button2 = ttk.Button(frame, text="No, click me!",
command=click_button2)

"""
Constructors for labels and text entry fields
.Label(parent, text)
.Entry(parent, width, textvariable[, state])
.Grid(column, row, columnspan, rowspan, sticky) 
"""

# Constructors and methods of the StringVar class
StringVar()
get()
set(str)

"""
Some methods of the messagebox module
showinfo(title, message)
showwarning(title, message)
showerror(title, message)
askyesno(title, message)
askokcancel(title, message)
"""
p