import tkinter as tk
from tkinter import ttk

first_window = tk.Tk()
first_window.title("⚾⚾⚾⚾⚾⚾⚾ Player ⚾⚾⚾⚾⚾⚾⚾")
first_window.geometry("400x300")

frame = ttk.Frame(first_window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


def cancel():
    first_window.destroy()


# Player ID grid
playerid_label = ttk.Label(frame, text="Player ID: ")
playerid_label.grid(column=0, row=0, sticky=tk.E)
playerid_text = tk.IntVar()
playerid_entry = ttk.Entry(frame, width=25, textvariable=playerid_text)
playerid_entry.grid(column=1, row=0, columnspan=2)
playerid_entry.delete(0, tk.END)

# First Name grid
first_name_label = ttk.Label(frame, text="First Name: ")
first_name_label.grid(column=0, row=1, sticky=tk.E)
first_name_text = tk.StringVar()
first_name_entry = ttk.Entry(frame, width=25, textvariable=first_name_text)
first_name_entry.grid(column=1, row=1, columnspan=2)

# Last Name grid
last_name_label = ttk.Label(frame, text="Last Name: ")
last_name_label.grid(column=0, row=2, sticky=tk.E)
last_name_text = tk.StringVar()
last_name_entry = ttk.Entry(frame, width=25, textvariable=last_name_text)
last_name_entry.grid(column=1, row=2, columnspan=2)

# Position grid
position_label = ttk.Label(frame, text="Position: ")
position_label.grid(column=0, row=3, sticky=tk.E)
position_text = tk.StringVar()
position_entry = ttk.Entry(frame, width=25, textvariable=position_text)
position_entry.grid(column=1, row=3, columnspan=2)

# At Bats grid
at_bats_label = ttk.Label(frame, text="At bats: ")
at_bats_label.grid(column=0, row=4, sticky=tk.E)
at_bats_text = tk.DoubleVar()
at_bats_entry = ttk.Entry(frame, width=25, textvariable=at_bats_text)
at_bats_entry.grid(column=1, row=4, columnspan=2)
at_bats_entry.delete(0, tk.END)

# Hits grid
hits_label = ttk.Label(frame, text="Hits: ")
hits_label.grid(column=0, row=5, sticky=tk.E)
hits_text = tk.StringVar()
hits_entry = ttk.Entry(frame, width=25, textvariable=hits_text)
hits_entry.grid(column=1, row=5, columnspan=2)

# Batting Avg
batting_avg_label = ttk.Label(frame, text="Batting Avg: ")
batting_avg_label.grid(column=0, row=6, sticky=tk.E)
batting_avg_text = tk.StringVar()
batting_avg_entry = ttk.Entry(frame, width=25, textvariable=batting_avg_text, state="readonly")
batting_avg_entry.grid(column=1, row=6, columnspan=2)

# Buttons
get_player_button = ttk.Button(frame, text="Get Player!")
get_player_button.grid(column=4, row=0)

save_changes_button = ttk.Button(frame, text="Save Changes")
save_changes_button.grid(column=1, row=7)

cancel_button = ttk.Button(frame, text="Cancel", command=cancel)
cancel_button.grid(column=2, row=7)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

first_window.mainloop()
