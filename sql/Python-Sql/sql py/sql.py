from DB import *

from tkinter import *
from tkinter.ttk import *

command = ['SHOW COLUMNS', 
           'FROM stocks']
 
data = RDB()
# data.execList(arr = command)


result = data.getColumnName()
# result = data.fetchall()
for row in result:
  print(row)
  



columns = []
for head in result:
  r =str(head)
  columns.append(r)
columns = tuple(columns)



root = Tk()
root.geometry('800x600')
root.title('SqlDB')

tree = Treeview(root, columns=columns, show='headings')
for col in columns:
  tree.heading(column=col, text=col)

for item in data.getData():
  tree.insert('',END, values=item)

tree.pack(fill='both', expand=True)


root.mainloop()

