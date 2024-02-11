from tkinter import *
from tkinter.ttk import Treeview
from tkinter.messagebox import showinfo


class Application:
    def __init__(self, name: str = "Application", MinSize: tuple[int,int] = (800,600) ,WinSize: str = "800x600"):
        self.app = Tk()
        self.app.title(name)
        # self.app.minsize(MinSize[0],MinSize[1])
        # self.app.geometry(WinSize)
        
    
    def Update(self):
        self.app.mainloop()

    def CreateLabel(self, text: str = "Label",):
        lbl = Label(self.app,text=text, height=15)
        lbl.grid(row=0, column=0, sticky='nsew')

    def CreateTable(self, contacts: list | tuple, columns: tuple[str] = ('id', 'medicament_Name', 'quantity', 'price')):
        tree = Treeview(self.app, columns=columns, show='headings')
        # define headings
        for val in columns:
            newVal = val.replace("_"," ")
            tree.heading(val, text=newVal.upper())
     
        # generate sample data
            # contacts = []
            # for n in range(1, 100):
            #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
        # add data to the treeview
        for contact in contacts:
            tree.insert('', END, values=contact)
        # tree.bind('<<TreeviewSelect>>', self.item_selected)
        # tree.grid(row=0, column=0, padx = 5, pady = 5)

        tree.grid(row=1, column=0, sticky='nsew')
        # add a scrollbar
        scrollbar = Scrollbar(self.app, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

    # def item_selected(self, event):
    #     for selected_item in self.tree.selection():
    #         item = self.tree.item(selected_item)
    #         record = item['values']
    #         # show a message
    #         showinfo(title='Information', message=','.join(record))
            
