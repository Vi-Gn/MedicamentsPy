from tkinter import ttk
import tkinter as tk
from dependencies.cursors import Cursors


class Tab(ttk.Notebook):
  def Init(self, row=0, column=1, sticky=tk.NSEW):
    self.grid(row=row, column=column, sticky=sticky)
    self.Frames: list[ttk.Frame] = []
    return self
  
  def CreateTableInNewTab(self, cols, datas, tabName='', height=300):
    '''Create new Table with frame In a NewTab'''
    Frame = ttk.Frame(self, height=height)
    self.add( Frame, text = tabName)
    self.Frames.append(Frame)
    table = TableData(Frame).Init(columns=cols, datas=datas, show='headings', cursor=Cursors.boat)
    
    return table

  def RenameTab(self, id: int, text: str):
    self.tab(id, text = text)
        
  def GetTabById(self, id: int):
    self.tabs[id]
    
    
class TableData(ttk.Treeview):
  def Init(self,
           columns,
           datas: list[any] | tuple[any],
           show='headings',
           cursor=Cursors.boat):
    #setup custom attributes
    self.columns = columns
    
    #setup default attributes
    self['columns'] = columns
    self['show'] = show
    self['cursor'] = cursor
    
    #setup headings and columns Structure
    for col in columns:
      self.heading(text=col, column=col, anchor='center')
      self.column(column=col, anchor='center', stretch=False, width=50)
    # self.heading(text='name', column='name', anchor='w')
    # self.column(column='name', anchor='w', stretch=True, width=100)
    
    #pack Table
    self.pack(fill='both', expand=1)
    
    # load Data and insert it in table
    for data in datas:      
      self.Insert(text=data[0], values=data)
    return self
        
  def SetColumns(self,
                  widths : list[int] | tuple[int], 
                  anchors : list[str] | tuple[str],
                  stretchs : list[bool] | tuple[bool]
                  ):
    '''setup headings and columns structure'''
    for i in range(len(self.columns)):
      self.heading(text=self.columns[i], column=self.columns[i], anchor=anchors[i])
      self.column(column=self.columns[i], anchor=anchors[i], stretch=stretchs[i], width=widths[i])

  def Insert(self, parent='', pos = "end", text = '', values= () ,open=True):
    self.insert(parent=parent, index=pos, text=text, values=values, open=open)
        
  # def Delete(self, id: str | int | list[str] | tuple[str] | list[int] | tuple[int]):
  #   '''delete children from id or list(id)'''
  #   for child in self.get_children():
  #     item_value = self.item(child, 'text')
  #     if str(item_value) in str(id):
  #       self.delete(child)




# from tkinter import ttk

# class TableData(ttk.Treeview):
#     def Init(self, columns, data: list[any] | tuple[any]):
#         for col in columns:
#             self.heading(text=col, column=col, anchor='center')
#             # self.column(column=col, anchor='center', stretch=True, width=100)
#         self.heading(text='name', column='name', anchor='w')
#         self.pack(fill='both', expand=1)
#         self.columns = columns
#         return self
        
#     def SetColumns(self,
#                    widths : list[int] | tuple[int], 
#                    anchors : list[str] | tuple[str],
#                    stretchs : list[bool] | tuple[bool]
#                    ):
#         for i in range(len(self.columns)):
#             self.column(column=self.columns[i],
#                         anchor=anchors[i],
#                         stretch=stretchs[i],
#                         width=widths[i])

#     def Insert(self, parent='', pos = "end", text = '', values= () ,open=True):
#         self.insert(parent=parent, index=pos, text=text, values=values, open=open)
        
#     def Delete(self, id):
#         for child in self.get_children():
#             item_value = self.item(child, 'values')[0]
#             if str(item_value) in str(id):
#                 self.delete(child)
