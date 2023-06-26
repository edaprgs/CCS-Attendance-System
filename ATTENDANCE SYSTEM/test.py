import tkinter as tk
from tkinter import messagebox

def event_menu():
    options = ["ADD EVENT", "EVENTS LIST"]
    def on_option_selected(value):
        messagebox.showinfo("Option Selected", f"You selected: {value}")
    menu = tk.Menu(tearoff=False)
    for option in options:  
        menu.add_command(label=option, command=lambda value=option: on_option_selected(value))
    menu.configure(font=("Tahoma", 12), bg="lightgoldenrod2", fg="black", activebackground="lightgoldenrod3", activeforeground="black")

    # Edit the width of the menu
    menu.configure(tearoffcommand=lambda: menu.winfo_width())

    x, y, _, _ = button.bbox(tk.ALL)
    x += button.winfo_rootx()
    y += button.winfo_rooty() + button.winfo_height()
    menu.post(x, y)

win = tk.Tk()

button = tk.Button(win, text="EVENTS", command=event_menu)
button.pack()

win.mainloop()



