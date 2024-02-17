import tkinter
from tkinter import filedialog
# from csvLib.csvLib import *
from file import *
from JS import *
from Application import *
from tkinter import simpledialog;

msg1 = '''

    1 - Insert an item
    2 - Remove an item
    3 - Modify an item
    4 - Show/Read items

'''

choice = 0

def fo():
    answer = simpledialog.askstring("title", "prompt")
    answer1 = simpledialog.askstring("title", "prompt")
    answer2 = simpledialog.askstring("title", "prompt")
    print(answer, answer1, answer2)

# name: str = "Application"


name = "Application"
columns: tuple[str] = ('id', 'medicament_Name', 'quantity', 'price')


def spawn():
    subApp = Toplevel(app)

def donothing():
    x = 0

# path = filedialog.askopenfilename()
# path = filedialog.asksaveasfilename()
def NewFile():
    # tempApp = Toplevel(app)
    
    # path = filedialog.askdirectory()
    # print(path)
    # d = DataManager(path)
    # DataRef = DataManager()
    # data1 = []
    # for ls in DataRef.GetData()['Meds']:
    #     data1.append(list(ls.values()))
    #     print(list(ls.values()))
    # length = len(list(data1)[0])
    # for contact in list(data1):
        # tree.insert('', END, values=contact)
    for i in tree.get_children():
        tree.delete(i)

def OpenNewFile():
    # tempApp = Toplevel(app)
    path = filedialog.askopenfilename()
    print(path)
    NewFile()
    DataRef = DataManager(path)
    data1 = []
    for ls in DataRef.GetData()['Meds']:
        data1.append(list(ls.values()))
        print(list(ls.values()))
    length = len(list(data1)[0])
    for contact in list(data1):
        tree.insert('', END, values=contact)

def SaveToFile():
    path = filedialog.asksaveasfilename()
    print(path)
    DataRef = DataManager(path)
    data1 = []
    for ls in DataRef.GetData()['Meds']:
        data1.append(list(ls.values()))
        print(list(ls.values()))
    length = len(list(data1)[0])
    for contact in list(data1):
        tree.insert('', END, values=contact)

if __name__ == '__main__':

    app = Tk()
    app.title(name)

    menu = Menu(app)
    filemenu = Menu(menu, tearoff=0)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open", command=OpenNewFile)
    filemenu.add_command(label="Save", command=SaveToFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=app.quit)
    menu.add_cascade(label="File", menu=filemenu)


    filemenu1 = Menu(menu, tearoff=0)
    menu.add_cascade(label="Edit", menu=filemenu1)
    filemenu1.add_command(label="AddItem", command=NewFile)
    filemenu1.add_command(label="RemoveItem", command=OpenNewFile)
    filemenu1.add_command(label="ModifyItem", command=SaveToFile)
    filemenu1.add_command(label="ReReadItem", command=SaveToFile)

    app.config(menu=menu)

    # btn = Button(app, text='Click', anchor="center", command=spawn)
    btn = Button(app, text='Click' , command=spawn)
    btn.grid(row=0, column=0)
  
    tree = Treeview(app,columns=columns, show="headings")
    for val in columns:
        newVal = val.replace('_',' ').upper()
        tree.heading(column=val, text=newVal,anchor="center")
    tree.grid(row=1, column=0)

    app.mainloop()


    # DataRef = DataManager()
    # data1 = []
    # for ls in DataRef.GetData()['Meds']:
    #     data1.append(list(ls.values()))
    #     print(list(ls.values()))
    

    # app = Application("Medicaments")
    # length = len(list(data1)[0])
    # app.CreateTable(contacts=list(data1))
    # app.CreateLabel()
    # btn = Button(app.app,command=fo, width="10", height="5",text="Add")
    # btn.grid(row=0,column=length,pady=0, padx=0,rowspan=50)
    # child_w= Toplevel(app.app)
    # app.Update()


    # DataRef = DataManager()
    # while True:
    #     Info(msg1)
    #     choice = int(input("Insert your choice"))
    #     match choice:
    #         case 1:
    #             tempName = Input("Insert the name of the new med")
    #             tempPrice = float(Input("Insert the price of the new med"))
    #             tempQuantity = int(Input("Insert the quantity of the new med"))
    #             DataRef.AddItemToFile(tempName, tempPrice, tempQuantity)
    #         case 2:
    #             tempName = Input("Insert the name of the med to delete")
    #             DataRef.RemoveItemByName(tempName)
    #         case 3:
    #             tempId = int(Input("Insert the id of the med"))
    #             tempName = Input("Insert the new name of the med")
    #             tempPrice = float(Input("Insert the new price of the med"))
    #             tempQuantity = int(Input("Insert the new quantity of the med"))
    #             DataRef.ModifyById(tempId, tempName, tempPrice, tempQuantity)
    #         case 4:
    #             DataRef.ReadItems()
    #         case _:
    #             Error("Choose again :)")

    #     if(choice == 5):
    #         break

    # 
    

  
