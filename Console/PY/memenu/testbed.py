import tkinter as tk
from tkinter import ttk
from typing import Literal
from dependencies.cursors import Cursors

from TableData import *
from menuSqlite import RDB


    
def setDarkTheme(themeName):
    """\"True = dark\" / \"False = light\""""
    root.tk.call("source", f"ForestTheme\\forest-{themeName}.tcl")
    style.theme_use( f"forest-{themeName}")


root = tk.Tk()
root.title('trying me new tab system under a nneew maanigment')
root.geometry("800x600")
root.grid_columnconfigure(0, minsize=200, weight= 1)
root.grid_columnconfigure(1, minsize=300, weight= 1)
root.grid_rowconfigure(0, minsize=200, weight= 1)
root.grid_rowconfigure(1, minsize=300, weight= 1)



Tabby1 = Tab(root).Init( row=0, column=0, sticky=tk.NSEW)

# leftFrame = ttk.Frame(root, height=300)
frame = ttk.Frame(root, height=300)
Tabby1.add(frame, text='Files')
tree1 = ttk.Treeview(frame, columns='files', show='headings')
tree1.heading(text='files', column='files', anchor='center')
tree1.pack(fill='both', expand=1)


database = RDB('Data/MedStocks.db')


Tabby = Tab(root).Init( row=0, column=1, sticky=tk.NSEW)

table = Tabby.CreateTableInNewTab( database.getColumnName(), database.getData(), 'MedStocks.db')

table.SetColumns((50, 100, 100, 50, 50), ('center','w','w','center','center'), (0,1,2,1,1))

database = RDB('Data/GeneratedData.db')

table1 = Tabby.CreateTableInNewTab( database.getColumnName(), database.getData(), 'GeneratedData.db')

table1.SetColumns((50, 100, 100, 50, 50), ('center','w','w','center','center'), (0,1,2,1,1))



# table = Tabby.CreateTabTable(
#     cols, [(1, 'Me', 99999), (2, 'Niko', 999), (3, 'Bellic', 999)], 'ef')
# table.SetColumns((50,100,50), ('center','w','center'), (0,1,0))
















style = ttk.Style(root)
# setDarkTheme('dark')
root.mainloop()










# import tkinter as tk
# from tkinter import ttk

# from tkinter import filedialog, simpledialog, messagebox


# class TableFrame(ttk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.parent = parent

# class MultiTab(ttk.Notebook):
#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.parent = parent

#     def addTab(self, tabClass, tab_name):
#         tab = tabClass(self)
#         self.add(tab, text=tab_name)

# class TabContent(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         label = tk.Label(self, text="This is content for the tab.")
#         label.pack()
        
# def setDarkTheme(themeName):
#     """\"True = dark\" / \"False = light\""""
#     root.tk.call("source", f"ForestTheme\\forest-{themeName}.tcl")
#     style.theme_use( f"forest-{themeName}")
#     # root.tk.call("source", f"ForestTheme\\forest-{themeName}.tcl")
#     # style.theme_use( f"ForestTheme\\forest-{themeName}")



# root = tk.Tk()
# root.title("Frame with Image Background")
# root.geometry('800x600')

# TableFrame(root, width = 150)

# style = ttk.Style(root)
# setDarkTheme('dark')



# root.mainloop()
