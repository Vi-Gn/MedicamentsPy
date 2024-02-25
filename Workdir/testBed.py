import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.messagebox import askyesno 
import src.csvLib as cfile

class App(tk.Tk):
    def __init__(self, title = "TreeView Example",width = 800, height = 600):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")



class Table(ttk.Treeview):
    def __init__(self, parent, columns = ('id', 'name', 'price', 'quantiity'), show ='headings'):
        super().__init__(master = parent, columns = columns, show = show, style='My.Treeview')
        self.columns = columns
        for col in columns:
            self.heading(column=col, text=col, anchor='center')
        for col in columns:
            self.column(col, anchor='center')
        self.Pack()
        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("My.Treeview", 
                            background='#ddd', 
                            foreground='#000', 
                            fieldbackground='#eee', 
                            borderwidth=0,
                            rowheight=25,
                            font=("Comic Sans MS", 10, "bold") )


        treestyle.configure("My.Treeview.Heading",
                            background='#333',
                            foreground='#eee',
                            fieldbackground='#444', 
                            borderwidth=0,
                            padding=5,
                            relief = 'flat',
                            font=("Comic Sans MS", 14, "bold") )
        
        treestyle.map('My.Treeview', 
                      background=[('selected', '#222')], 
                      foreground=[('selected', '#eee')])
        
        treestyle.map('My.Treeview.Heading', 
                      background=[('active', '#eee')], 
                      foreground=[('active', '#333')])

        parent.bind("<<TreeviewSelect>>", self.select)
        parent.bind('<Double-1>', self.doubleclick)
        self.parent = parent

    def select(self, event=None):
        selected_items = self.selection()  # Get the IDs of selected items
        for item in selected_items:
            item_value = tree.item(item, "value")  # Get the text of each selected item
            print("Selected item:", item_value)
        # self.search.focus_force()
        print('')

    def Append(self, parentId = '', values = ('1', 'Doli', '50', '25')):
        self.insert(parentId, tk.END, values=values)
        
    def Pack(self, fill='both', expand=True):
        self.pack(fill=fill, expand=expand)

    def doubleclick(self, event):
        selected_items = self.selection() 
        active_item = self.identify('item', event.x, event.y)
        col = self.identify_column(event.x)
        col = int(col[1:])
        col_index = col - 1
        print(col_index)
        for item in selected_items:
            self.selection_remove(item)
        self.selection_add(active_item)
        self.entryfield(active_item, col_index)

    def entryfield(self, item, col_index):
        # subWindow = Toplevel(self.parent, width=300, height=200)
        # lbl = tk.Label(subWindow, text='Id', anchor='center')
        # lbl.pack(subWindow)
        bb = self.bbox(item, col_index)
        field = tk.Entry(self.parent)
        field.place(x= bb[0], y= bb[1], width=bb[2], height=bb[3])
        field.bind("<Return>", lambda e : self.modify(field, item, col_index))
        

    def modify(self, field: tk.Entry, item, col_index):
        text = field.get()
        
        self.set(item, column=col_index, value=text)

        field.destroy()
        # print(col_index)
        # self.item(item, values=('54','dedor', '50', '69'))
        # self.set(item, values=('54','dedor', '50', '69'))

        # (item, column='id', value='1')
        # self.set(item, column='name', value='wdwd')
        # self.set(item, column='price', value='5454')
        # self.set(item, column='quantity', value='69')
        
    # def doubleclick(self, event):
    #     children = event.widget.selection()
    #     for child in children:
    #         item = event.widget.item(child)
    #         value = item['values']
    #         print(value)

    def loadcsv(self, path: str = 'Data/data.csv'):
        for child in self.get_children():
            self.delete(child)
        for line in cfile.ReadCSV(path):
            tree.Append(values=(line['id'], line['name'], line['price'], line['quantity']))
    

class Search(tk.Entry):
    def __init__(self, parent, table: Table):
        super().__init__(master=parent)
        self.table = table
        self.searchText = tk.StringVar(parent)
        self.searchText.trace_add("write", self.callback)
        self.search = tk.Entry(root, textvariable=self.searchText, foreground='#111', background='#eee')
        self.search.pack(fill='both', expand=True)
        self.search.bind('<Return>', self.callbackReturn)

    def callbackReturn(self, *event):
        self.table.loadcsv()
        self.table.selection_remove(self.table.get_children())
        for child in self.table.get_children():            
            item = self.table.item(child)
            values = item['values']
            if(self.search.get() != '' and not(values[1].lower().startswith(self.search.get().lower()))):
                self.table.delete(child)    
                # self.table.selection_add(child)
        self.search.focus_force()


    def callback(self, *event):
        self.table.selection_remove(self.table.get_children())
        for child in self.table.get_children():                
            item = self.table.item(child)
            values = item['values']
            if(self.search.get() != '' and values[1].startswith(self.search.get())):
                self.table.selection_add(child)
        self.search.focus_force()

        
        
def save(event):
    vals = []
    for item in tree.get_children():
        vals.append(tree.item(item)['values'])
    print(vals)
    cfile.OverriteCSV(vals, 'Data/genData.csv')

# Create the main window

root = App()

root.bind('<Control-s>', save)
tree = Table(parent=root)
tree.loadcsv('Data/genData.csv')




searchBar = Search(root, tree)

# search.bind("<Key>", )

# print(askyesno('Confirm', 'Do you want to save?'))
# print(askyesno('Confirm', 'Do you want to save?'))
root.mainloop()







# # Create a Treeview widget
# tree = ttk.Treeview(root)
# tree.pack()

# # Insert some items into the Treeview
# tree.insert("", "end", text="Item 1")
# tree.insert("", "end", text="Item 2")
# tree.insert("", "end", text="Item 3")

# # Bind the TreeviewSelect event to the selection function
# tree.bind("<<TreeviewSelect>>", selection)

















# import os
# import tkinter as tk
# from tkinter import ttk

# def populate_tree(tree, node, path):
#     """
#     Recursively populate the Treeview widget with directories and subdirectories.

#     Args:
#     - tree: Treeview widget to populate.
#     - node: Parent node ID.
#     - path: Directory path.
#     """
#     # Iterate over directories in the current path
#     for dir_name in os.listdir(path):
#         print(dir_name)
#         dir_path = os.path.join(path, dir_name)
#         # Add directory to the Treeview
#         node_id = tree.insert(node, "end", text=dir_name, open=False)
#         # If the current item is a directory, recursively populate its subdirectories
#         if os.path.isdir(dir_path):
#             populate_tree(tree, node_id, dir_path)
  
            
            

# # Create the main window
# root = tk.Tk()
# root.title("Directory TreeView Example")

# # Create a Treeview widget
# tree = ttk.Treeview(root)
# tree.pack(expand=True, fill=tk.BOTH)

# # Get the list of directories (replace 'your_directory_path' with the actual directory path)
# directory_path = os.path.abspath('')
# # Ensure the directory exists
# if os.path.exists(directory_path) and os.path.isdir(directory_path):
#     # Populate the Treeview with directories and subdirectories
#     populate_tree(tree, "", directory_path)
# else:
#     print("Directory does not exist.")

# root.mainloop()
