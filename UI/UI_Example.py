from future_value import get_future_value, get_years, get_interest_rate, get_monthly_investment
import locale as lc
import tkinter as tk
from tkinter import ttk


def calculate_future_value():
    try:
        monthly_investment = float(name_text.get())
        interest_rate = float(about_text.get())
        years = int(years_text.get())

        future_value = get_future_value(monthly_investment, interest_rate, years)

        future_value_label.config(text=lc.currency(future_value, grouping=True))
    except ValueError:
        future_value_label.config(text="Invalid input")


def clicked_button2():
    first_window.destroy()

# Create an empty window
first_window = tk.Tk()
first_window.title("Future Value Calculator")
first_window.geometry("400x300")

frame = ttk.Frame(first_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


name_label = ttk.Label(frame, text="Monthly Investment")
name_label.grid(column=0, row=0, sticky=tk.E)
name_text = tk.DoubleVar()
name_entry = ttk.Entry(frame, width=25, textvariable=name_text)
name_entry.grid(column=1, row=0)

about_label = ttk.Label(frame, text="Yearly Interest Rate")
about_label.grid(column=0, row=1, sticky=tk.E)
about_text = tk.DoubleVar()
about_entry = ttk.Entry(frame, width=25, textvariable=about_text)
about_entry.grid(column=1, row=1)

years_label = ttk.Label(frame, text="Years")
years_label.grid(column=0, row=2, sticky=tk.E)
years_text = tk.IntVar()
years_entry = ttk.Entry(frame, width=25, textvariable=years_text)
years_entry.grid(column=1, row=2)

future_value_label = ttk.Label(frame, text="")
future_value_label.grid(column=0, row=3)
future_value_text = tk.DoubleVar()
future_value_entry = ttk.Entry(frame, width=25, textvariable=future_value_text, state="readonly")
future_value_entry.grid(column=1, row=3)

calculate_button = ttk.Button(frame, text="Calculate!", command=calculate_future_value())
calculate_button.grid(column=0, row=4)
button2 = ttk.Button(frame, text="Exit!", command=clicked_button2)
button2.grid(column=1, row=4)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)


first_window.mainloop()
