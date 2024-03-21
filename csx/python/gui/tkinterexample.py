import tkinter as tk
from tkinter import ttk

def incvalue():
    progress_var.set(progress_var.get() + 1)

def decvalue():
    progress_var.set(progress_var.get() - 1)


root = tk.Tk()

progress_var = tk.DoubleVar()
progress_var.set(50)

frm = ttk.Frame(root, padding=20)

frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

ttk.Combobox(frm, values=["A", "B", "C"]).grid(column=0, row=1)

ttk.Progressbar(frm, orient="horizontal", length=200, variable=progress_var).grid(column=1, row=1)


ttk.Button(frm, text="< - >", command=decvalue).grid(column=0, row=2)
ttk.Button(frm, text="< + >", command=incvalue).grid(column=1, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=3)



root.mainloop()


