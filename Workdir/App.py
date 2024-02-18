
import os
from tkinter import filedialog
from tkinter.ttk import *

from src.csvLib import *

from tkinter import *

def list_folders_files(directory: str) -> list[str]:
    result = []
    
    for root, dirs, files in os.walk(directory):
        for f in files:
            result.append(os.path.join(root, f))
    return result

def ClearTable():
    for i in ap.treeTable.get_children():
        ap.treeTable.delete(i)

def ClearFileTable():
    for i in ap.treeFile.get_children():
        ap.treeFile.delete(i)

def NewDir():
    # os.path.abspath(f"../{self.workdirName}")
    ap.workdir = filedialog.askdirectory().replace("/", "\\")
    # ap.workdir.replace("\\", "/")

    ap.app.title(ap.title + "         " + ap.workdir)
    ClearFileTable()
    ap.InitDir()
    # print(ap.workdir, '-----------------')

def NewFile():
    ap.file = filedialog.askopenfilename(initialdir=ap.workdir)
    ClearTable()
    # print(ap.file)


def OpenFile(path: str = ''):
    # tempApp = Toplevel(app)
    if path == '':
        ap.file = filedialog.askopenfilename(initialdir=ap.workdir)
    else:
        ap.file = path
    # print(ap.file)
    ClearTable()

    DataRef = ReadCSV(path=ap.file)
    # print(DataRef)
    data1 = []
    for ls in DataRef:
        data1.append(list(ls.values()))
        # print(list(ls.values()))
    length = len(list(data1)[0])
    for contact in list(data1):
        ap.treeTable.insert('', END, values=contact)

def OpenDirLoaded():
    # path = filedialog.askdirectory(initialdir=ap.workdir)
    path = os.path.abspath('..\\')
    node_id = ap.treeFile.insert('', "end", text=ap.workdirName, values= path ,open=False)
    OpenDir(node_id)

def OpenDir(node = '', path = os.path.abspath('..\\Workdir')):
    # Iterate over directories in the current path
    for dir_name in os.listdir(path):
        # print(dir_name)
        dir_path = os.path.join(path, dir_name)
        value = dir_path.replace('\\', '/')
        
        # Add directory to the Treeview
        node_id = ap.treeFile.insert(node, "end", text=dir_name, values= value ,open=False)
        # If the current item is a directory, recursively populate its subdirectories
        if os.path.isdir(dir_path):
            OpenDir(node_id, dir_path)
  


class TableApplication:
    def __init__(self, title: str, resX: int, resY: int, iconPath = 'Icon/meds.ico') -> None:
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
        # self.app.minsize(width= 800, height= 450)
        # self.app.maxsize(width= 895, height= 450)
        self.workdirName = 'Workdir'
        self.workdir = os.path.abspath(f"../{self.workdirName}")
        self.fileName = 'Data/data.csv'
        self.filepath = os.path.abspath(f"{self.fileName}")
        # print(self.filepath)
        self.AddFileMenu()
        self.app.bind("<Configure>", self.on_window_resize)
        self.mainFrame = LabelFrame(self.app, text="App")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)
        self.mainFrame.pack(fill="both", padx=5, pady=5, expand=1)
        

        

    def on_window_resize(self, event):
        self.winWidth = int(event.width)
        self.winHeight = int(event.height)

    '''
        # print(self.winWidth)
        # self.treeTable.column('id', width = (self.winWidth // 5), stretch = False, anchor="center")
        # self.treeTable.column('name', width= (self.winWidth * 2 // 5), stretch = False, anchor="center")
        # self.treeTable.column('quantity', width = (self.winWidth // 5), stretch = False, anchor="center")
        # self.treeTable.column('price', width = (self.winWidth // 5), stretch = False, anchor="center")
        # # if(self.winWidth != event.width):
        #     self.winWidth = event.width
        #     self.frametable.config(width= int(event.width))

        # # if(self.winHeight != event.height):
        #     self.winHeight = event.height
        
    
    # def AddFileMenu(self):
    #     self.menu = Menu(self.app)
    #     filemenu = Menu(self.menu, tearoff=0)
    #     filemenu.add_command(label="New File", command=NewFile)
    #     filemenu.add_command(label="New Directory", command=NewDir)
    #     filemenu.add_command(label="Open File", command=OpenFile)
    #     filemenu.add_command(label="Open Directory", command='')
    #     filemenu.add_command(label="Save File", command='')
    #     filemenu.add_separator()
    #     filemenu.add_command(label="Exit", command=self.app.quit)
    #     self.menu.add_cascade(label="File", menu=filemenu)
    #     self.app.config(menu=self.menu)
    '''
    def AddFileMenu(self):
        menu = Menu(self.app)
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label="New File", command=NewFile)
        filemenu.add_command(label="New Directory", command=NewDir)
        filemenu.add_command(label="Open File", command=OpenFile)
        filemenu.add_command(label="Open Directory", command=OpenDirLoaded)
        filemenu.add_command(label="Save File", command='''SaveFile''')
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.app.quit)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu1 = Menu(menu, tearoff=0)
        filemenu1.add_command(label="AddItem", command='')
        filemenu1.add_command(label="RemoveItem", command='')
        filemenu1.add_command(label="ModifyItem", command='')
        filemenu1.add_command(label="ReloadItems", command='')
        menu.add_cascade(label="Edit", menu=filemenu1)
        self.app.config(menu=menu)
        # To do
        # filemenu.add_command(label="New Directory", command='''NewFile''')
        # To do
        # filemenu.add_command(label="Open Directory", command='''OpenNewFile''')
    def InitFile(self):
        ap.file = self.filepath
        # print(ap.file)
        ClearTable()

        DataRef = ReadCSV(path=ap.file)
        # print(DataRef)
        data1 = []
        for ls in DataRef:
            data1.append(list(ls.values()))
            # print(list(ls.values()))
        length = len(list(data1)[0])
        for contact in list(data1):
            ap.treeTable.insert('', END, values=contact)

        
    def InitDir(self):
        

        files: list[str] = []
        for i in list_folders_files(self.workdir):
            temp = i.replace(os.path.abspath("..\\")+"\\", "")
            temp = temp.replace("\\", "/")
            files.append(temp)
        filesArr: list[str]= []
        for i in files:
            if i.endswith('.csv'):
                filesArr.append(i.split("/"))
        
        
        # print(filesArr)
        # self.treeFile.insert(parent="",index='end', text=filesArr[0][0], values='', iid=0)
        # self.treeFile.insert(parent=0,index='end', text=filesArr[0][1], values='', iid=1)
        # self.treeFile.insert(parent=1,index='end', text=filesArr[0][2], values='', iid=2)
        # self.treeFile.insert(parent=1,index='end', text=filesArr[1][2], values='', iid=3)

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
        self.InitDir()
        OpenDir()
        self.InitFile()
        
    def get_selected_item_Data(self, event):        
        selected_items = self.treeTable.selection()  # Get the IDs of selected items
        for item in selected_items:
            item_text = self.treeTable.item(item, "value")  # Get the value of each selected item
            print("Selected item:", item_text)
        
    def get_selected_item_File(self, event):        
        selected_items = self.treeFile.selection()  # Get the IDs of selected items
        for item in selected_items:
            item_text = self.treeFile.item(item, "value")[0]  # Get the value of each selected item
            children = self.treeFile.get_children(item)
            if len(children) == 0:
                if(str(item_text).endswith(".csv")):
                    print("Openning file:", item_text)
                    OpenFile(item_text)
                else:
                    print("Can't open file:", item_text)


    def InitTable(self, columns: tuple[str] = ('id', 'name', 'quantity', 'price')):
        self.frametable = Frame(self.mainFrame, width = 150)
        self.treeTable = Treeview(self.frametable,columns=columns, show="headings", selectmode='extended')
        self.treeTable.bind("<<TreeviewSelect>>", self.get_selected_item_Data)
        for val in columns:
            newVal = val.replace('_',' ').upper()
            self.treeTable.heading(column=val, text=newVal,anchor=CENTER)
            
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


columns: tuple[str] = ('id', 'medicament_Name', 'quantity', 'price')

if __name__ == '__main__':
    ap = TableApplication("Hands Of Mine", 895,600)
    ap.InitTable()
    ap.FileManager()
    s= Style()

    s.theme_use(s.theme_names()[6])
    # s.configure("Treeview",
    #     background="#D3D3D3",
    #     foreground="black",
    #     rowheight=25,
    #     fieldbackground="#D3D3D3"       
    # )
    s.map("Treeview",
        background=[('selected', '#347083')])
    ap.Update()
