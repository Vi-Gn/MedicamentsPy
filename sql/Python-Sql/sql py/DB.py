import mysql.connector as DB

def Warn(**kwarg):
  print(kwarg)

class RDB():
  def __init__(self, user: str = 'root', password: str = 'M@ddieel123', host: str = 'localhost', database: str = 'medicaments', raise_on_warnings: bool = True):
    config = {
      'user': user,
      'password': password,
      'host': host,
      'database': database,
      'raise_on_warnings': raise_on_warnings
      }
    self.database = DB.connect(**config)
    self.cursor = self.database.cursor()
    self.result = ''
    self.colnames = self.getColumnName()
    self.data = self.getData()
  
  def execLinesFetched(self, *lines):
    '''fetch all from exec without altering current cursor value'''
    cmd = ''
    for line in lines:
      cmd += ' ' + line 
    self.cursor.execute(cmd)
    return self.cursor.fetchall()

  def execLines(self, *lines):
    cmd = ''
    for line in lines:
      cmd += ' ' + line 
    self.cursor.execute(cmd)

  def execListFetched(self, arr: list[str]):
    '''fetch all from exec without altering current cursor value'''
    cmd = ' '.join(arr)
    self.cursor.execute(cmd)
    return self.cursor.fetchall()

  def execList(self, arr: list[str]):
    cmd = ' '.join(arr)
    self.cursor.execute(cmd)

  def apply(self):
    Warn("You have commited to the database")
    self.database.commit()

  def fetchAll(self):
    self.result = self.cursor.fetchall()
    return self.result

  def fetchOne(self):
    self.result = self.cursor.fetchone()
    return self.result

  def getColumnName(self):
    temp = self.execLinesFetched('SHOW COLUMNS', 'FROM stocks')
    self.colnames = []
    self.colnames.clear()
    for elem in temp:
      self.colnames.append(elem[0])
    return self.colnames
  
  def getData(self):
    self.data = self.execLinesFetched('SELECT *', 'FROM stocks')
    return self.data