import tkinter as tk
from tkinter import ttk



class File():
  @staticmethod
  def NewFile(root):
    top = tk.Toplevel(root)
    
    name = ttk.Entry(top, )
    name.pack(fill="x", expand=True, padx=5,pady=5)
    
    btn = ttk.Button(top,text='reload', command=lambda: [ self.newFileAction(name), top.destroy()], padding=5)
    btn.pack(fill="x", expand=True)
    # open()