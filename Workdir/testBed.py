import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno 


class App(tk.Tk):
    def __init__(self, title = "TreeView Example",width = 800, height = 600):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")



class Table(ttk.Treeview):
    def __init__(self, parent, columns = ('id', 'name', 'price', 'quantiity'), show ='headings'):
        super().__init__(master = parent, columns = columns, show = show, style='My.Treeview')
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

        parent.bind("<<TreeviewSelect>>", lambda event: root.focus_set())

    def Append(self, parentId = '', values = ('1', 'Doli', '50', '25')):
        self.insert(parentId, tk.END, values=values)
        
    def Pack(self, fill='both', expand=True):
        self.pack(fill=fill, expand=expand)

def get_selection(event=None):
    selected_items = tree.selection()  # Get the IDs of selected items
    for item in selected_items:
        item_text = tree.item(item, "text")  # Get the text of each selected item
        print("Selected item:", item_text)

# Create the main window

root = App()

tree = Table(parent=root)

tree.Append(values=('1', 'Doli', '50', '25'))
tree.Append(values=('1', 'Doli', '50', '25'))
tree.Append(values=('1', 'Doli', '50', '25'))
tree.Append(values=('1', 'Doli', '50', '25'))

search = tk.Entry(root, foreground='#111', background='#eee')
search.pack(fill='both', expand=True)

print(askyesno('Confirm', 'Do you want to save?'))
print(askyesno('Confirm', 'Do you want to save?'))
root.mainloop()







# # Create a Treeview widget
# tree = ttk.Treeview(root)
# tree.pack()

# # Insert some items into the Treeview
# tree.insert("", "end", text="Item 1")
# tree.insert("", "end", text="Item 2")
# tree.insert("", "end", text="Item 3")

# # Bind the TreeviewSelect event to the get_selection function
# tree.bind("<<TreeviewSelect>>", get_selection)

















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
