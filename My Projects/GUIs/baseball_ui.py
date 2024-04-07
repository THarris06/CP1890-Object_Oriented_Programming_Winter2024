import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

window = tk.Tk()
window.title("Player")
window.geometry("400x300")

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)


def clicked_save_button():
    print("clicked_save_button")


def clicked_cancel_button():
    window.destroy()


def clicked_getPlayer_button():
    conn = sqlite3.connect("baseball_database.db")
    c = conn.cursor()
    query = "SELECT * FROM Players WHERE id = ?"
    c.execute(query, playerId_text.get())
    rows = c.fetchone()
    conn.close()
    firstName_text.set(rows[1])
    lastName_text.set(rows[2])
    position_text.set(rows[3])
    atBats_text.set(rows[4])
    hits_text.set(rows[5])
    average_text.set(rows[5] / rows[4])


# Labels
playerId_label = ttk.Label(frame, text="Player ID:")
playerId_label.grid(row=0, column=0, sticky=tk.E)

firstName_label = ttk.Label(frame, text="First name:")
firstName_label.grid(row=1, column=0, sticky=tk.E)

lastName_label = ttk.Label(frame, text="Last name:")
lastName_label.grid(row=2, column=0, sticky=tk.E)

position_label = ttk.Label(frame, text="Position:")
position_label.grid(row=3, column=0, sticky=tk.E)

atBats_label = ttk.Label(frame, text="At bats:")
atBats_label.grid(row=4, column=0, sticky=tk.E)

hits_label = ttk.Label(frame, text="Hits:")
hits_label.grid(row=5, column=0, sticky=tk.E)

average_label = ttk.Label(frame, text="Batting Avg:")
average_label.grid(row=6, column=0, sticky=tk.E)

# Entries
playerId_text = tk.StringVar()
playerId_input = ttk.Entry(frame, width=25, textvariable=playerId_text)
playerId_input.grid(row=0, column=1, columnspan=2)

firstName_text = tk.StringVar()
firstName_input = ttk.Entry(frame, width=25, textvariable=firstName_text)
firstName_input.grid(row=1, column=1, columnspan=2)

lastName_text = tk.StringVar()
lastName_input = ttk.Entry(frame, width=25, textvariable=lastName_text)
lastName_input.grid(row=2, column=1, columnspan=2)

position_text = tk.StringVar()
position_input = ttk.Entry(frame, width=25, textvariable=position_text)
position_input.grid(row=3, column=1, columnspan=2)

atBats_text = tk.IntVar()
atBats_input = ttk.Entry(frame, width=25, textvariable=atBats_text)
atBats_input.grid(row=4, column=1, columnspan=2)

hits_text = tk.IntVar()
hits_input = ttk.Entry(frame, width=25, textvariable=hits_text)
hits_input.grid(row=5, column=1, columnspan=2)

average_text = tk.StringVar()
average_input = ttk.Entry(frame, width=25, textvariable=average_text, state="readonly")
average_input.grid(row=6, column=1, columnspan=2)

# Buttons
save_button = ttk.Button(frame, text="Save Changes", command=clicked_save_button)
save_button.grid(column=1, row=7)

cancel_button = ttk.Button(frame, text="Cancel", command=clicked_cancel_button)
cancel_button.grid(column=2, row=7)

getPlayer_button = ttk.Button(frame, text="Get Player", command=clicked_getPlayer_button)
getPlayer_button.grid(column=3, row=0)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=3)

window.mainloop()
