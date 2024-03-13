
import os

from menuSqlite import RDB


class Application():
  def __init__(self, iconPath = 'Icon/meds.ico') -> None:
    # initialize databases files name
    self.fileName: list[str] = []
    self.fileName.append('MedStocks.db')
    
    # load databases
    self.data: RDB = []
    self.data.append(RDB(self.fileName))
    
    self.filepath = os.path.abspath(f"Data/")
    
    self.databaseTable = 'stocks'
    # self.data.createTable(self.databaseTable)
    # self.data.save()
    
    
    
Application()