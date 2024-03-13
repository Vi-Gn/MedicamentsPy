import tkinter as tk
from tkinter import ttk
from TopLevelCentered import TopLevelCentered
from menuSqlite import *
import dependencies.style as style



from PIL import Image, ImageTk




########
import os
from tkinter import filedialog, simpledialog


def ClearFileTable():
    for i in ap.treeFile.get_children():
        ap.treeFile.delete(i)


def empty():
    0
    
    
err = None
def OpenDir(node = '', path = os.path.abspath('Data')):
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
        err = tk.Toplevel(ap.app)
        
        err.grab_set()
        err.protocol("WM_DELETE_WINDOW", empty)
        errMessage = ttk.Label(err, text="Path invalid please retry!")
        btn = ttk.Button(err,text='reload', command=lambda : [OpenDirLoaded(), err.destroy()])
        btnClose = ttk.Button(err,text='exit', command=lambda : ap.app.destroy())
        errMessage.pack(fill="both")
        btn.pack(fill="both")
        btnClose.pack(fill="both")
        

def OpenDirLoaded(dirNAme: str = '', shouldAsk: bool = True):
    
    print("Im done with this maaan!!-_-")
    if shouldAsk:
        path = filedialog.askdirectory(initialdir=ap.workdir)
    else:
        path = ap.workdir
    # if path == '':
        # path = os.path.abspath('')
    
    print(path)
    
    ClearFileTable()
    path = path.replace("\\", "/")
    if dirNAme == '':
        dirName = path.split("/")[-1]
    # path = os.path.abspath('')
    node_id = ap.treeFile.insert('', "end", text=dirName, values= (path,) ,open=True, tags="Parent")
    OpenDir(node_id, path)
    
def ClearTable():
  for i in ap.treeTable.get_children():
      ap.treeTable.delete(i)

#########


# class TableData(ttk.Treeview):
#     def Init(self):
#         return self


# TableData()



class TableApplication:
    def __init__(self, title: str, resX: int, resY: int, iconPath = 'Icon/meds.ico') -> None:
        self.fileName = 'Data/MedStocks.db'
        self.filepath = os.path.abspath(f"{self.fileName}")
        self.data = RDB(self.fileName)
        self.databaseTable = 'stocks'
        self.data.createTable(self.databaseTable)
        self.data.save()
        self.app = tk.Tk()
        
        self.style = ttk.Style(self.app)
        # self.setDarkTheme('dark')
        self.setDarkTheme('light')

        # self.app.configure(bg='#000')
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
        self.app.minsize(width= 1024, height= 450)
        # self.app.maxsize(width= 680, height= 450)
        self.workdirName = 'Data'
        self.workdir = os.path.abspath(f"{self.workdirName}")
        
        # print(self.filepath)
        self.AddFileMenu()
        self.app.bind("<Configure>", self.on_window_resize)
        self.mainFrame = ttk.LabelFrame(self.app, text="App")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, minsize=250, weight=0)
        self.mainFrame.grid_columnconfigure(1, minsize=700, weight=1)
        self.mainFrame.pack(fill="both", padx=5, pady=5, expand=1)
                
    def setDarkTheme(self, themeName):
        """\"True = dark\" / \"False = light\""""
        self.style.tk.call("source", f"ForestTheme\\forest-{themeName}.tcl")
        self.style.theme_use( f"forest-{themeName}")

        
    def newFileAction(self, name):
        fName = name.get()
        f = open(self.workdir + '/' + fName+'.db','w')
        f.close()
        OpenDirLoaded('', False)
        
        # self.InitFile()
        #   raise Exception('make it clean')
        
      
    def newFile(self):
        # top = tk.Toplevel(self.app)
        top = TopLevelCentered(self.app).Init('Add')
        
        ttk.Label(top, text='Enter the file name').pack(fill="x", expand=True, ipadx=35, padx=15, pady=5)
        
        name = ttk.Entry(top)
        name.pack(fill="x", expand=True, ipadx=35, padx=15, pady=5)
        # inp = name.
        
        btn = ttk.Button(top,text='reload', command=lambda: [ self.newFileAction(name), top.destroy()], padding=5)
        btn.pack(fill="x", expand=True, ipadx=35, padx=15, pady=5)
        # open()

    def on_window_resize(self, event):
        self.winWidth = int(event.width)
        self.winHeight = int(event.height)
      
    def checkWhatToChange(self , lbl, dsc, qtt, prc, answer:str ='') -> str:
        '''asks if should change attributes'''
        if answer=='':
            top = tk.Toplevel(self.app, padx=5, pady=5, width=340, height=200)
            
            btnQ = ttk.Button(top,text='Add Quantity', command=lambda : [self.checkWhatToChange(lbl, dsc, qtt, prc,'q'), top.destroy()])
            btnQ.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
            btnP = ttk.Button(top,text='Override Price', command=lambda: [self.checkWhatToChange(lbl, dsc, qtt, prc,'p'), top.destroy()])
            btnP.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
            btnQP = ttk.Button(top,text='Add Quatity & Override Price', command=lambda: [self.checkWhatToChange(lbl, dsc, qtt, prc,'qp'), top.destroy()])
            btnQP.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)
            
            btnCancel = ttk.Button(top,text='Cancel', command=lambda: top.destroy())
            btnCancel.grid(row=0, column=3, sticky=tk.NSEW, padx=5, pady=5)
        else:
            DataAdder().addMenuUI(self.data ,lbl, dsc, qtt, prc, answer)
            self.InitFile()
            return
        # dialog = simpledialog.SimpleDialog(self.app,
        #                                text=msg,
        #                                buttons=["AddQuantity", "ChangePrice", "Both"],
        #                                title="Choose Option")
        # choice = dialog.go()
        # match (choice):
        #     case (0):
        #         return 'q'
            
        #     case (1):
        #         return 'p'
            
        #     case (2):
        #         return 'qp'
            
            

        
    def addItemAction(self, Labelle, Description, Quantity, Price):
        lbl = Labelle.get()
        dsc = Description.get()
        qtt = Quantity.get()
        prc = Price.get()
        labelNoFound = DataAdder().addMenuUICheck(self.data, lbl)
        if labelNoFound == True:
            DataAdder().addMenuUI(self.data ,lbl, dsc, qtt, prc, '')
            self.InitFile()
        else:
            self.checkWhatToChange(lbl, dsc, qtt, prc, '')
        

    def addItem(self):
        top = tk.Toplevel(self.app, padx=5, pady=5, width=340, height=200)
        lbl1 = ttk.Label(top, text="Enter Labelle")
        lbl1.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        Labelle = ttk.Entry(top)
        Labelle.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)
        lbl2 = ttk.Label(top, text="Enter Description")
        lbl2.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        Description = ttk.Entry(top)
        Description.grid(row=1, column=1, sticky=tk.NSEW, padx=5, pady=5)
        lbl3 = ttk.Label(top, text="Enter Quantity")
        lbl3.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)
        Quantity = ttk.Entry(top)
        Quantity.grid(row=1, column=2, sticky=tk.NSEW, padx=5, pady=5)
        lbl4 = ttk.Label(top, text="Enter Price")
        lbl4.grid(row=0, column=3, sticky=tk.NSEW, padx=5, pady=5)
        Price = ttk.Entry(top)
        Price.grid(row=1, column=3, sticky=tk.NSEW, padx=5, pady=5)
        # inp = Labelle.
        
        btnAdd = ttk.Button(top,text='Add', command=lambda: self.addItemAction(Labelle, Description, Quantity, Price))
        btnAdd.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)
        btnCancel = ttk.Button(top,text='Cancel', command=lambda: top.destroy())
        btnCancel.grid(row=2, column=2, sticky=tk.NSEW, padx=5, pady=5)
        
    def removeItem(self, *args):
        selected_items = self.treeTable.selection()  # Get the IDs of selected items
        for item in selected_items:
            id: int = self.treeTable.item(item, "value")[0]  # Get the value of each selected item
            self.data.removeByRef(id)
        self.InitFile()
    
    def modifyItem(self):
        print('\n\n\nException : not done yet\n\n\n')
        exit(5)

    def AddFileMenu(self):
        menu = tk.Menu(self.app)
        filemenu = tk.Menu(menu, tearoff=0)
        filemenu.add_command(label="New File", command=self.newFile)
        filemenu.add_command(label="Reload File", command=self.InitFile)
        # filemenu.add_command(label="Open File", command='OpenFile')
        filemenu.add_command(label="Open Directory", command='self.OpenDir')
        filemenu.add_command(label="Save File", command='''SaveFile''')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.app.quit)
        menu.configure(bg="black", fg="white", font=("Arial", 12))
        menu.add_cascade(label="File", menu=filemenu)
        filemenu1 = tk.Menu(menu, tearoff=0)
        filemenu1.add_command(label="AddItem", command=self.addItem)
        filemenu1.add_command(label="RemoveItem", command=self.removeItem)
        filemenu1.add_command(label="ModifyItem", command=self.modifyItem)
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
        # ap.file = self.filepath
        # print(ap.file)

        ClearTable()
        
        self.data = None
        self.data = RDB(self.fileName)
        self.databaseTable = 'stocks'

        self.data.createTable(self.databaseTable)
        self.data.save()
        items = self.data.getData()
        for item in items:
          self.treeTable.insert('', tk.END, values=item)
            
 

    def FileManager(self, columns: tuple[str] = ('#0',)):
        self.frameFile = ttk.Frame(self.mainFrame, width = 150)
        self.treeFile: ttk.Treeview = ttk.Treeview(self.frameFile, selectmode="browse")
        self.treeFile.bind("<<TreeviewSelect>>", self.get_selected_item_File)
        

        self.treeFile.heading(column='#0', text='File',anchor="center")
        
     
        
        scrollbarV = ttk.Scrollbar(self.frameFile, orient=tk.VERTICAL, command=self.treeFile.yview)
        
       
        
        self.treeFile.configure(yscroll = scrollbarV.set)
        scrollbarV.pack(fill="both", side=tk.RIGHT)
        
        scrollbarH = ttk.Scrollbar(self.frameFile, orient=tk.HORIZONTAL, command=self.treeFile.xview)
        self.treeFile.configure(xscroll=scrollbarH.set)
        scrollbarH.pack(fill="both", side=tk.BOTTOM)
       
        
        
        self.treeFile.pack(fill="both", padx=5, pady=5, expand=1)
        self.frameFile.grid(row=0, column=0, sticky=tk.NSEW)
        # self.InitDir()
        OpenDirLoaded()
        # self.InitFile()
        
    def get_selected_item_Data(self, event):        
        selected_items = self.treeTable.selection()  # Get the IDs of selected items
        for item in selected_items:
            item_value = self.treeTable.item(item, "value")  # Get the value of each selected item
            print("Selected item:", item_value)
        
    # def get_selected_item_File(self, event):    
    #     self.InitFile()
      
    def get_selected_item_File(self, event):        
        selected_items = self.treeFile.selection()  # Get the IDs of selected items
        for item in selected_items:
            item_value = self.treeFile.item(item, "value")[0]
            try:
                print('sccccccccccccccccccccccccccccs', self.treeFile.item(item, "tags"))
                isParent = self.treeFile.item(item, "tags")[0] == 'Parent'
                 # Get the value of each selected item
                if(isParent):
                    print('Can only Open files')
                    return
            except IndexError as e:
                print('(get_selected_item_File(), item.tags)contains no tag')
            
            
            self.fileName = os.path.relpath(item_value)
            self.InitFile()
            '''
            # children = self.treeFile.get_children(item)
            # if len(children) == 0:
            #     if(str(item_value).endswith(".db")):
            #         print("Openning file:", item_value)
            #         print(item)
            #         'OpenFile(item_value)'
            #     else:
            #         print("Can't open file:", item_value)
'''

    def InitTable(self):
        self.frametable = ttk.Frame(self.mainFrame, width = 150)
        columns = self.data.getColumnName()
        self.treeTable: ttk.Treeview = ttk.Treeview(self.frametable,columns=columns, show="headings", selectmode='extended')
        self.treeTable.bind("<<TreeviewSelect>>", self.get_selected_item_Data)
        self.treeTable.bind("<Delete>", self.removeItem)
        for val in columns:
            newVal = val.replace('_',' ').upper()
            self.treeTable.heading(column=val, text=newVal,anchor=tk.CENTER)
        self.treeTable.column(columns[0], width = 50, stretch = False, anchor="center")
        # self.treeTable.column('name', minwidth = 100, stretch = False, anchor="w")
        self.treeTable.column(columns[-2], width = 100, stretch = False, anchor="center")
        self.treeTable.column(columns[-1], width = 100, stretch = False, anchor="center")
        
        scrollbarV = ttk.Scrollbar(self.frametable, orient=tk.VERTICAL, command=self.treeTable.yview)
        self.treeTable.configure(yscroll=scrollbarV.set)
        scrollbarV.pack(fill="y", side=tk.RIGHT)
        
        scrollbarH = ttk.Scrollbar(self.frametable, orient=tk.HORIZONTAL, command=self.treeTable.xview)
        self.treeTable.configure(xscroll=scrollbarH.set)
        scrollbarH.pack(fill="x", side=tk.BOTTOM)

       
        
        self.treeTable.pack(fill="both", padx=5, pady=5, expand=1)
        self.frametable.grid(row=0, column=1, sticky=tk.NSEW)
    

    def Update(self):
        self.app.mainloop()


    

# setDarkTheme('dark')
# setDarkTheme('light')
ap = TableApplication("Hands Of Mine", 895,600)
ap.InitTable()
ap.FileManager()

########################        
style = ttk.Style()
# style.theme_use('default')
style.configure("Vertical.TScrollbar", gripcount=100, background="red", troughcolor="blue", gripcolor="yellow")
# scrollbarV.config(style="Custom.Vertical.TScrollbar")        
########################
########################      
style.configure("Horizontal.TScrollbar", gripcount=15, background="red", troughcolor="blue", gripcolor="yellow")

########################

    
ap.Update()



