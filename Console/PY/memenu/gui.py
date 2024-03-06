from tkinter import *
from tkinter.ttk import *
from menuSqlite import *
import dependencies.style as style

########
import os
from tkinter import filedialog


def ClearFileTable():
    for i in ap.treeFile.get_children():
        ap.treeFile.delete(i)


def empty():
    0
    
    
err = NONE
def OpenDir(node = '', path = os.path.abspath('..\\Workdir')):
    # Iterate over directories in the current path
    try:
        for dir_name in os.listdir(path):
            dir_name.split('.')
            # print(dir_name)
            dir_path = os.path.join(path, dir_name)
            value = dir_path.replace('\\', '/')
            
            # Add directory to the Treeview
            node_id = ap.treeFile.insert(node, "end", text=dir_name, values= value ,open=False)
            # If the current item is a directory, recursively populate its subdirectories
            if os.path.isdir(dir_path):
                OpenDir(node_id, dir_path)
    except:
        print(" folder not valid ")
        global err
        err = Toplevel(ap.app)
        
        err.grab_set()
        err.protocol("WM_DELETE_WINDOW", empty)
        errMessage = Label(err, text="Path invalid please retry!")
        btn = Button(err,text='reload', command=lambda : [OpenDirLoaded(), err.destroy()])
        btnClose = Button(err,text='exit', command=lambda : ap.app.destroy())
        errMessage.pack(fill="both")
        btn.pack(fill="both")
        btnClose.pack(fill="both")
        

def OpenDirLoaded(dirNAme: str = ''):
    
    path = filedialog.askdirectory(initialdir=ap.workdir)
        
    # if path == '':
        # path = os.path.abspath('')
    
    
    ClearFileTable()
  
    if dirNAme == '':
        dirName = path.split("/")[-1]
    # path = os.path.abspath('')
    node_id = ap.treeFile.insert('', "end", text=dirName, values= path ,open=False)
    OpenDir(node_id, path)
    
def ClearTable():
  for i in ap.treeTable.get_children():
      ap.treeTable.delete(i)

#########


class TableApplication:
    def __init__(self, title: str, resX: int, resY: int, iconPath = 'Icon/meds.ico') -> None:
        self.fileName = 'Data/MedStocks.db'
        self.filepath = os.path.abspath(f"{self.fileName}")
        self.data = RDB(self.fileName)
        self.databaseTable = 'stocks'
        self.data.createTable(self.databaseTable)
        self.app = Tk()
        # self.app.configure(bg="grey80")
        self.title = title
        self.winWidth = resX
        self.winHeight = resY
        self.app.state("zoomed")
        # self.app.attributes("-fullscreen", True)
        self.resolution = f"{resX}x{resY}"
        self.app.title(self.title)
        self.app.iconbitmap(iconPath)
        self.app.geometry(self.resolution)
        self.app.minsize(width= 680, height= 450)
        # self.app.maxsize(width= 680, height= 450)
        self.workdirName = 'Data'
        self.workdir = os.path.abspath(f"{self.workdirName}")
        
        # print(self.filepath)
        self.AddFileMenu()
        self.app.bind("<Configure>", self.on_window_resize)
        self.mainFrame = LabelFrame(self.app, text="App")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)
        self.mainFrame.pack(fill="both", padx=5, pady=5, expand=1)
        
    def newFileAction(self, name):
      fName = name.get()
      f = open(self.workdir + '/' + fName+'.db','w')
      raise Exception('make it clean')
      f.close()
      
    def newFile(self):
        top = Toplevel(self.app)
        
        name = Entry(top)
        name.pack(fill="x", expand=True)
        # inp = name.
        
        btn = Button(top,text='reload', command=lambda: [ self.newFileAction(name), top.destroy()])
        btn.pack(fill="x", expand=True)
        # open()

    def on_window_resize(self, event):
        self.winWidth = int(event.width)
        self.winHeight = int(event.height)

    def AddFileMenu(self):
        menu = Menu(self.app)
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label="New File", command=self.newFile)
        filemenu.add_command(label="Reload File", command=self.InitFile)
        filemenu.add_command(label="Open File", command='OpenFile')
        filemenu.add_command(label="Open Directory", command='self.OpenDir')
        filemenu.add_command(label="Save File", command='''SaveFile''')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.app.quit)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu1 = Menu(menu, tearoff=0)
        # filemenu1.add_command(label="AddItem", command=self.add)
        filemenu1.add_command(label="RemoveItem", command='')
        filemenu1.add_command(label="ModifyItem", command='')
        filemenu1.add_command(label="ReloadItems", command='')
        menu.add_cascade(label="Edit", menu=filemenu1)
        self.app.config(menu=menu)
        # To do
        # filemenu.add_command(label="New Directory", command='''NewFile''')
        # To do
        # filemenu.add_command(label="Open Directory", command='''OpenNewFile''')
    # def InitFile(self):
    #     ap.file = self.filepath
    #     # print(ap.file)
    #     ClearTable()

    #     DataRef = ReadCSV(path=ap.file)
    #     # print(DataRef)
    #     data1 = []
    #     for ls in DataRef:
    #         data1.append(list(ls.values()))
    #         # print(list(ls.values()))
    #     length = len(list(data1)[0])
    #     for contact in list(data1):
    #         ap.treeTable.insert('', END, values=contact)
    
    def InitFile(self):
        ap.file = self.filepath
        # print(ap.file)
        ClearTable()

        items = self.data.getData()
        for item in items:
          self.treeTable.insert('', END, values=item)
            
 

    def FileManager(self, columns: tuple[str] = ('#0')):
        self.frameFile = Frame(self.mainFrame, width = 150)
        self.treeFile = Treeview(self.frameFile, selectmode="browse")
        self.treeFile.bind("<<TreeviewSelect>>", self.get_selected_item_File)

        self.treeFile.heading(column='#0', text='File',anchor="center")
        scrollbarV = Scrollbar(self.frameFile, orient=VERTICAL, command=self.treeFile.yview)
        self.treeFile.configure(yscroll=scrollbarV.set)
        scrollbarV.pack(fill="both", side=RIGHT)
        
        scrollbarH = Scrollbar(self.frameFile, orient=HORIZONTAL, command=self.treeFile.xview)
        self.treeFile.configure(xscroll=scrollbarH.set)
        scrollbarH.pack(fill="both", side=BOTTOM)

        self.treeFile.pack(fill="both", padx=5, pady=5, expand=1)
        self.frameFile.grid(row=0, column=0, sticky=NSEW)
        # self.InitDir()
        OpenDirLoaded()
        self.InitFile()
        
    def get_selected_item_Data(self, event):        
        selected_items = self.treeTable.selection()  # Get the IDs of selected items
        for item in selected_items:
            item_text = self.treeTable.item(item, "value")  # Get the value of each selected item
            print("Selected item:", item_text)
        
    # def get_selected_item_File(self, event):    
    #     self.InitFile()
      
    def get_selected_item_File(self, event):        
        selected_items = self.treeFile.selection()  # Get the IDs of selected items
        for item in selected_items:
            item_text = self.treeFile.item(item, "value")[0]  # Get the value of each selected item
            children = self.treeFile.get_children(item)
            
            
            self.fileName = os.path.relpath(item_text)
            self.InitFile()
            # if len(children) == 0:
            #     if(str(item_text).endswith(".db")):
            #         print("Openning file:", item_text)
            #         print(item)
            #         'OpenFile(item_text)'
            #     else:
            #         print("Can't open file:", item_text)


    def InitTable(self):
        self.frametable = Frame(self.mainFrame, width = 150)
        columns = self.data.getColumnName()
        self.treeTable = Treeview(self.frametable,columns=columns, show="headings", selectmode='extended')
        self.treeTable.bind("<<TreeviewSelect>>", self.get_selected_item_Data)
        for val in columns:
            newVal = val.replace('_',' ').upper()
            self.treeTable.heading(column=val, text=newVal,anchor=CENTER)
        self.treeTable.column(columns[0], width = 50, stretch = False, anchor="center")
        # self.treeTable.column('name', minwidth = 100, stretch = False, anchor="w")
        self.treeTable.column(columns[-2], width = 100, stretch = False, anchor="center")
        self.treeTable.column(columns[-1], width = 100, stretch = False, anchor="center")
        
        scrollbarV = Scrollbar(self.frametable, orient=VERTICAL, command=self.treeTable.yview)
        self.treeTable.configure(yscroll=scrollbarV.set)
        scrollbarV.pack(fill="y", side=RIGHT)
        
        scrollbarH = Scrollbar(self.frametable, orient=HORIZONTAL, command=self.treeTable.xview)
        self.treeTable.configure(xscroll=scrollbarH.set)
        scrollbarH.pack(fill="x", side=BOTTOM)

       
        
        self.treeTable.pack(fill="both", padx=5, pady=5, expand=1)
        self.frametable.grid(row=0, column=1, sticky=NSEW)
    

    def Update(self):
        self.app.mainloop()


ap = TableApplication("Hands Of Mine", 895,600)
ap.InitTable()
ap.FileManager()
ap.Update()


# root = Tk()
print('Window\'s Created!')
# root.geometry("800x600")
# root.title('Gestion de Medicament')



print('Frame\'s Created!')
# mainFrame = Frame(master=root, style='mainFrame.TFrame')
# mainFrame.pack(fill='both', expand=True)


print("Create a table")
# cols: list[str] = data.getColumnName();
# tableData = Treeview(master=mainFrame, columns=cols, show='headings', style='tableData.Treeview', selectmode='browse')
# for col in cols:
#   tableData.column(col, stretch=True, anchor='center')
#   textCol = col.capitalize()
#   tableData.heading(column=col, text=textCol)
# tableData.pack(padx=5, pady=5, fill='both', expand=True)
# items = data.getData()
# for item in items:
#   tableData.insert('', END, values=item)
  
# def onselect(e):
#   selectedItems = tableData.selection()
#   for item in selectedItems:
#     print(tableData.item(item, 'values'))
    
  
# tableData.bind('<<TreeviewSelect>>', onselect)


style.StyleApp()


print('Window\'s Loop Started!')
# root.mainloop()



