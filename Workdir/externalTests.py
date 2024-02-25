import tkinter as tk
from tkinter import messagebox, ttk

def show_info():
    # Get the text of the item whose Id is stored in `my_iid`.
    text = treeview.item(my_iid, option="text")
    # Display it within a message box.
    messagebox.showinfo(title="Item Info", message=text)

root = tk.Tk()
root.title("Treeview in Tk")
treeview = ttk.Treeview()
my_iid = "unique_id"
treeview.insert("", tk.END, text="Item 1", iid=my_iid)
treeview.pack()
button = ttk.Button(text="Show info", command=show_info)
button.pack()
root.mainloop()