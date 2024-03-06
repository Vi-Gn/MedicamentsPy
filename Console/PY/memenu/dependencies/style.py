
from tkinter.ttk import Style

def StyleApp():
  print('Style\'s Constructed!')
  style = Style()
  style.theme_use('default')
  # style.configure('mainFrame.TFrame', background = '#000', foreground = '#eee')
  style.configure('tableData.Treeview', 
                              background='#ddd', 
                              foreground='#000', 
                              fieldbackground='#eee', 
                              borderwidth=0,
                              rowheight=25,
                              font=("Comic Sans MS", 8, "bold") )

  style.configure('tableData.Treeview.Heading', 
                              background='#333',
                              foreground='#eee',
                              fieldbackground='#444', 
                              borderwidth=0,
                              padding=2,
                              relief = 'flat',
                              font=("Comic Sans MS", 11, "bold") )

  style.map('tableData.Treeview',  
                              background=[('selected', '#222')], 
                              foreground=[('selected', '#eee')])

  style.map('tableData.Treeview.Heading', 
                              background=[('active', '#eee')], 
                              foreground=[('active', '#333')])
