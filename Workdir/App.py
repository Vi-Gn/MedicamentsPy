
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
    print(ap.workdir, '-----------------')

def NewFile():
    ap.file = filedialog.askopenfilename(initialdir=ap.workdir)
    ClearTable()
    print(ap.file)


def OpenFile():
    # tempApp = Toplevel(app)
    ap.file = filedialog.askopenfilename(initialdir=ap.workdir)
    print(ap.file)
    ClearTable()

    DataRef = ReadCSV(path=ap.file)
    print(DataRef)
    data1 = []
    for ls in DataRef:
        data1.append(list(ls.values()))
        print(list(ls.values()))
    length = len(list(data1)[0])
    for contact in list(data1):
        ap.treeTable.insert('', END, values=contact)




class TableApplication:
    def __init__(self, title: str, resX: int, resY: int, iconPath = 'Icon/meds.ico') -> None:
        self.app = Tk()
        # self.app.configure(bg="grey80")
        self.title = title
        self.winWidth = resX
        self.winHeight = resY
        self.resolution = f"{resX}x{resY}"
        self.app.title(self.title)
        self.app.iconbitmap(iconPath)
        self.app.geometry(self.resolution)
        # self.app.minsize(width= 800, height= 450)
        # self.app.maxsize(width= 895, height= 450)
        self.workdirName = 'Workdir'
        self.workdir = os.path.abspath(f"../{self.workdirName}")
        self.AddFileMenu()
        self.app.bind("<Configure>", self.on_window_resize)
        self.mainFrame = LabelFrame(self.app, text="App")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)
        self.mainFrame.pack(fill="both", padx=5, pady=5)

        

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
        filemenu.add_command(label="Open Directory", command='''OpenNewFile''')
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
    def InitDir(self):
        # filedialog.askopenfilenames(initialdir=self.workdir)
        # print((self.workdir))
        # self.files = [os.path.join(self.workdir, item) for item in os.listdir(self.workdir)]
        # for i in self.files:
        #     print(i)
        # print(self.workdir)
        files: list[str] = []
        for i in list_folders_files(self.workdir):
            temp = i.replace(os.path.abspath("..\\")+"\\", "")
            temp = temp.replace("\\", "/")
            files.append(temp)
        filesArr: list[str]= []
        for i in files:
            if i.endswith('.csv'):
                filesArr.append(i.split("/"))
        
        
        print(filesArr)
        self.treeFile.insert(parent="",index='end', text=filesArr[0][0], values='', iid=0)
        self.treeFile.insert(parent=0,index='end', text=filesArr[0][1], values='', iid=1)
        self.treeFile.insert(parent=1,index='end', text=filesArr[0][2], values='', iid=2)
        self.treeFile.insert(parent=1,index='end', text=filesArr[1][2], values='', iid=3)
        # self.treeFile.insert(parent=0,index='end', text="", values='----'+filesArr[1][1], iid=2)
        # self.treeFile.insert(parent=0,index='end', text="", values='----'+filesArr[2][1], iid=3)
        # self.treeFile.insert(parent=3,index='end', text="", values='--------'+filesArr[2][2], iid=0.1)
        
        # for file in filesArr:
            
        #     for i in range(len(file)):
        #         self.treeFile.insert(file[0],END, values=file[i])

        # self.treeFile.insert('', END,values='fil', iid='5')
        # self.treeFile.insert('fil', END,values='filsc')
        # self.treeFile.insert('5', END, values='data')
        # self.treeFile.insert('5', END, values='data')
        # self.treeFile.insert('data', END, values='cy.mouk')

    def FileManager(self, columns: tuple[str] = ('#0')):
        # self.frameFile = LabelFrame(self.mainFrame, text= "Files", width = 150)
        self.treeFile = Treeview(self.mainFrame)
        # self.treeFile['columns'] = columns
        self.treeFile.heading(column='#0', text='File',anchor="center")
        # self.treeFile.heading(column='#0', text='',anchor="center")

        # self.treeFile.column('#0', stretch = True, width = 120, minwidth=25)
        # self.treeFile.column('', width = 200, stretch = True)
        
        scrollbarV = Scrollbar(self.mainFrame, orient=VERTICAL, command=self.treeFile.yview)
        self.treeFile.configure(yscroll=scrollbarV.set)
        scrollbarV.grid(row=0, column=1, sticky='ns')
        
        scrollbarH = Scrollbar(self.mainFrame, orient=HORIZONTAL, command=self.treeFile.xview)
        self.treeFile.configure(xscroll=scrollbarH.set)
        scrollbarH.grid(row=1, column=0, sticky='ew')


        # self.treeFile.pack(fill="both", padx=5, pady=5)
        self.treeFile.grid(row=0, column=0, sticky=NSEW)
        self.InitDir()
        # self.frameFile.pack(fill="both", side='left', padx=5, pady=5)

    def InitTable(self, columns: tuple[str] = ('id', 'name', 'quantity', 'price')):
        # self.frame = LabelFrame(self.mainFrame, text= "Data", background="#000", foreground="#fff", border="1")
        
        # self.frametable = LabelFrame(self.mainFrame, text= "Data")
        # self.frametable.bind("<Configure>", self.on_window_resize)
       
        self.treeTable = Treeview(self.mainFrame,columns=columns, show="headings", selectmode='extended')
        for val in columns:
            newVal = val.replace('_',' ').upper()
            self.treeTable.heading(column=val, text=newVal,anchor=CENTER)
        # self.treeTable.column('id', width = 80, stretch = True, anchor="center")
        # self.treeTable.column('name', stretch = True, anchor="center")
        # self.treeTable.column('quantity', width = 120, stretch = True, anchor="center")
        # self.treeTable.column('price', width = 120, stretch = True, anchor="center")
        # self.treeTable.pack(fill="both", padx=5, pady=5)
        self.treeTable.grid(row=0, column=2, sticky=NSEW)
        # self.frametable.pack(fill="both", side="right", padx=5, pady=5)
        # (row=0, column=0, padx=5, pady=5, ipadx=50, ipady=50)
        # self.tableWidth = IntVar()

    def Update(self):
        self.app.mainloop()


columns: tuple[str] = ('id', 'medicament_Name', 'quantity', 'price')

if __name__ == '__main__':
    ap = TableApplication("Hands Of Mine", 895,600)
    # ap.InitTable()
    ap.FileManager()
    s= Style()

    s.theme_use('default')
    s.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3"       
    )
    s.map("Treeview",
        background=[('selected', '#347083')])
    ap.Update()
