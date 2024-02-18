import tkinter as tk
from tkinter import ttk

def get_selection(event=None):
    selected_items = tree.selection()  # Get the IDs of selected items
    for item in selected_items:
        item_text = tree.item(item, "text")  # Get the text of each selected item
        print("Selected item:", item_text)

# Create the main window
root = tk.Tk()
root.title("TreeView Example")

# Create a Treeview widget
tree = ttk.Treeview(root)
tree.pack()

# Insert some items into the Treeview
tree.insert("", "end", text="Item 1")
tree.insert("", "end", text="Item 2")
tree.insert("", "end", text="Item 3")

# Bind the TreeviewSelect event to the get_selection function
tree.bind("<<TreeviewSelect>>", get_selection)

root.mainloop()































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
