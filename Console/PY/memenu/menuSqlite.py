import sqlite3


# data = sqlite3.connect('MedStocks.db')
# table = 'stocks'
# create_table = """ CREATE TABLE IF NOT EXISTS projects (
  
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         name text NOT NULL,
#                         begin_date text,
#                         end_date text
                        
#                     ); """
                                    
# data.execute(f"create table {table} (id INTEGER PRIMARY KEY AUTOINCREMENT,\
#                                     name VARCHAR(25),\
#                                     price FLOAT,\
#                                     quantity INT\
#                                     )\
#                                     ")

# data.execute(f"INSERT INTO  {table}(name, price, quantity)\
#               VALUES ( 'hmd', 0.0, 99999)"
#             )
#
# data.commit()
#
# cursor = data.execute( f"SELECT * FROM {table}")
# print(cursor.fetchall())



def warn(*kwarg):
  print(kwarg)


class RDB():
    def __init__(self, databaseName: str = 'MedStocks.db') -> None:
      self.databaseName = databaseName
      self.database = sqlite3.connect(databaseName)
      self.cursor = self.database.cursor()
      self.table = 'stocks'
      # self.colnames = self.getColumnName()
      # self.data = self.getData()

    def __del__(self):
      print('wdwdwd')
      pass
      # self.database.
    
    def createTable(self, table: str = 'stocks') -> None:
      self.table = table
      try:
          self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS {table} (

                              ref INTEGER PRIMARY KEY AUTOINCREMENT,
                              labelle VARCHAR(50) NOT NULL,
                              description VARCHAR(50),
                              quantity INT,
                              price FLOAT

                  );
          """)

          self.save()
      except Exception as e:
          print('wdwd',e)

    def save(self):
      print(f"DB : {self.databaseName} has been saved successfully")
      self.database.commit()

    def insertWithRef(self, ref: int, labelle: str, description: str, quantity: int, price: float):
      raise Exception("still hasn't implemented yet!")
      self.execLines("INSERT INTO stocks",
                            f"VALUES ( {ref}, '{labelle}', '{description}', {quantity}, {price})")
      # self.save()

    def insert(self, labelle: str, description: str, quantity: int, price: float):
        self.execLines("INSERT INTO stocks(labelle, description, quantity, price)",
                              f"VALUES ( '{labelle}', '{description}', {quantity}, {price})")
        self.save()

    def execLinesFetched(self, *lines):
        """fetch all from exec without altering current cursor value"""
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
        """fetch all from exec without altering current cursor value"""
        cmd = ' '.join(arr)
        self.cursor.execute(cmd)
        return self.cursor.fetchall()

    def execList(self, arr: list[str]):
        cmd = ' '.join(arr)
        self.cursor.execute(cmd)

    def fetchAll(self):
        return self.cursor.fetchall()

    def fetchOne(self):
        return self.cursor.fetchone()

    def getColumnName(self):
        temp = self.execLinesFetched( f'SELECT name FROM PRAGMA_TABLE_INFO("{self.table}");')
        
        self.colnames = []
        for elem in temp:
            self.colnames.append(elem[0])
        return self.colnames

    def getData(self, cols: str = '*'):
        self.cursor.execute(f'SELECT {cols} FROM {self.table}')
        return self.cursor.fetchall()

    def getRef(self, ref: int, cols: str = '*'):
        if not(self.existsRef(ref)):
            print(f"{ref =} doesn't exist")
            return
        self.cursor.execute(f'SELECT {cols} FROM {self.table} WHERE ref={ref}')
        return self.cursor.fetchone()

    def getLabelle(self, labelle: str, cols: str = '*'):
        if not(self.existsLabelle(labelle)):
            print(f"{labelle =} doesn't exist")
            return
        self.cursor.execute(f'SELECT {cols} FROM {self.table} WHERE labelle="{labelle}"')
        return self.cursor.fetchone()

    def getLabelleContain(self, labelle: str, cols: str = '*'):
        if not(self.existsLabelleContain(labelle)):
            print(f"{labelle =} doesn't exist")
            return
        self.cursor.execute(f"SELECT {cols} FROM {self.table} WHERE labelle like'%{labelle}%'")
        return self.cursor.fetchall()

    def modifyAllByRef(self, ref: int, labelle: str, description: str, quantity: int, price: float):
        if not(self.existsRef(ref)):
            print(f"{ref =} doesn't exist")
            return
        update = f''' UPDATE {self.table}
                   SET labelle = "{labelle}" ,
                       description = "{description}" ,
                       quantity = {quantity} ,
                       price = {price}
                   WHERE ref = {ref};
        '''
        self.cursor.execute(update)
        self.save()

    def modifyColByRef(self, ref: int, col, content):
        if not(self.existsRef(ref)):
            print(f"{ref =} doesn't exist")
            return
        update = f''' UPDATE {self.table}
                   SET {col} = "{content}" 
                   WHERE ref = {ref};
        '''
        self.cursor.execute(update)
        self.save()

    def modifyColByLabelle(self, labelle: str, col, content):
        if not(self.existsLabelle(labelle)):
            print(f"{labelle =} doesn't exist")
            return
        print(f"labelle cond : {labelle}, col name : {col}, its content : {content}")
        update = f''' UPDATE {self.table}
                   SET {col} = "{content}" 
                   WHERE labelle = "{labelle}";
        '''
        self.cursor.execute(update)
        self.save()

    def modifyAllByLabelle(self, oldLabel: str, labelle: str, description: str, quantity: int, price: float):
        if not(self.existsLabelle(oldLabel)):
            print(f"{labelle =} doesn't exist")
            return
        update = f''' UPDATE {self.table}
                   SET labelle = "{labelle}" ,
                       description = "{description}" ,
                       quantity = {quantity} ,
                       price = {price}
                   WHERE labelle = '{oldLabel}';
        '''
        self.cursor.execute(update)
        self.save()

    

    def removeAll(self):
        self.cursor.execute(f"DELETE FROM {self.table};")
        self.save()
        
    def removeByRef(self, ref: int):
        if not(self.existsRef(ref)):
            print(f"{ref =} doesn't exist")
            return
        self.cursor.execute(f"DELETE FROM {self.table} WHERE ref = {ref};")
        self.save()
        
    def removeByLabelle(self, labelle: str):
        if not(self.existsLabelle(labelle)):
            print(f"{labelle =} doesn't exist")
            return
        self.cursor.execute(f"DELETE FROM {self.table} WHERE labelle = '{labelle}';")
        self.save()

    def checkForQuantityByRef(self, ref: int, quantity: int):
        if not(self.existsRef(ref)):
            print(f"{ref =} doesn't exist")
            return
        return (self.getRef(ref, 'quantity')[0] >= quantity)

    def checkForQuantityByLabelle(self, labelle: str, quantity: int):
        if not(self.existsLabelle(labelle)):
            print(f"{labelle =} doesn't exist")
            return False
        return (self.getLabelle(labelle, 'quantity')[0] >= quantity)

    def consumeByRef(self, ref: int, quantity: int):
        if not(self.existsRef(ref)):
            print(f"{ref =} doesn't exist")
            return
        hasQuantity = self.checkForQuantityByRef(ref, quantity)
        if hasQuantity == False:
            print("We Don't have this much quantity")
            return
        update = f''' UPDATE {self.table}
                           SET quantity = quantity - {quantity}
                           WHERE ref = {ref};
                '''
        self.cursor.execute(update)
        self.save()
        
    def consumeByLabelle(self, labelle: str, quantity: int):
        if not(self.existsLabelle(labelle)):
            print(f"{labelle =} doesn't exist")
            return
        hasQuantity = self.checkForQuantityByLabelle(labelle, quantity)
        if hasQuantity == False:
            print("We Don't have this much quantity")
            return
        update = f''' UPDATE {self.table}
                                   SET quantity = quantity - {quantity}
                                   WHERE labelle = "{labelle};
                        '''
        self.cursor.execute(update)
        self.save()

    def addQuantityByRef(self, ref: int, quantity: int):
        if not(self.existsRef(ref)):
            print(f"{ref =} doesn't exist")
            return
        update = f''' UPDATE {self.table}
                           SET quantity = quantity + {quantity}
                           WHERE ref = {ref};
                '''
        self.cursor.execute(update)
        self.save()
        
    def addQuantityByLabelle(self, labelle: str, quantity: int):
        if not(self.existsLabelle(labelle)):
            print(f"{labelle =} doesn't exist")
            return
        update = f''' UPDATE {self.table}
                                   SET quantity = quantity + {quantity}
                                   WHERE labelle = "{labelle}";
                        '''
        self.cursor.execute(update)
        self.save()

    def printData(self, cols: str = '*'):
        for item in self.getData(cols):
            print(item)

    def existsRef(self, ref: int):
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table} WHERE ref={ref}")
        return self.cursor.fetchone()[0] > 0

    def existsLabelle(self, labelle: str):
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table} WHERE labelle='{labelle}'")
        return self.cursor.fetchone()[0] > 0

    def existsLabelleContain(self, labelle: str):
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table} WHERE labelle like'%{labelle}%'")
        return self.cursor.fetchone()[0] > 0

class DataShower:
  msgshow: str = '''
          1 - Full
          2 - labelle
          3 - description
          4 - quantity
          5 - price
          0 - back
  '''
  
  @staticmethod
  def showMenu():
    print('''show''')
    menu = int(input(DataShower.msgshow))
    match (menu):
      case (1):
        DataShower.showAll()
      case (2):
        DataShower.showlabelle()
      case (3):
        DataShower.showDescription()
      case (4):
        DataShower.showQuantity()
      case (5):
        DataShower.showPrice()
      case (0):
        return
        

  @staticmethod
  def showAll():
      print('''all''')
      for item in data.getData('*'):
            print(item)
      

  @staticmethod
  def showlabelle():
      print('''labelle''')
      for item in data.getData('labelle'):
            print(item)

  @staticmethod
  def showDescription():
      print('''description''')
      for item in data.getData('description'):
            print(item)
      

  @staticmethod
  def showQuantity():
      print('''quantity''')
      for item in data.getData('quantity'):
            print(item)

  @staticmethod
  def showPrice():
      print('''price''')
      for item in data.getData('price'):
            print(item)
      
class DataAdder:
  msgaddstock: str = '''
        1 - ref
        2 - labelle
        0 - back
  '''
  @staticmethod
  def addMenu(ldata = None, labelle: str = '', description: str = '', quantity: int = 0, price: float = 0.0, action: str=''):
    """@action => p = add price; q = modify price; qp = both"""
    global data
    print('''add''')
    if labelle == '':
      labelle = input('Enter labelle')
    if ldata != None:
        data = ldata
    if data.existsLabelle(labelle):
      if ( action == ''):
        action = input(f'label {labelle} already exists if you want to add a quantity enter q; if want to change price enter p; if both enter qp')

      match (action):
        case ('q'):
          if(quantity == 0):
            quantity = int(input('Enter quantity to add'))
          data.addQuantityByLabelle(labelle, quantity)
          print(f'the item with name : {labelle} got an addition in quantity by {quantity}')
          return
        case ('p'):
          if(price == 0.0):
            price = float(input('Important! Erase old Price; Enter the new price'))
          data.modifyColByLabelle(labelle, 'price', price)
          print(f'the item\'s new price = {price}')
          return
        case ('qp'):
          if(quantity == 0):
            quantity = int(input('Enter quantity to add'))
          if(price == 0.0):
            price = float(input('Important! Erase old Price; Enter the new price'))
          data.addQuantityByLabelle(labelle, quantity)
          print(f'the item with name : {labelle} got an addition in quantity by {quantity}')
          data.modifyColByLabelle(labelle, 'price', price)
          print(f'the item\'s new price = {price}')
          return
        case _:
          raise Exception('action should not be different than p, q, qp')
      

    if description == '':
      description = input('Enter description')
    if quantity == 0:
      quantity = int(input('Enter quantity'))
    if price == 0.0:
      price = float(input('Enter price'))
    
      
    data.insert(labelle, description, quantity, price)
    
    
    
  @staticmethod
  def addMenuUICheck(ldata = None, labelle: str = ''):
    """ @function shall return => p = add price; q = modify price; qp = both """
    global data
    print('''add''')
    if ldata != None:
        data = ldata
    if data.existsLabelle(labelle):
      return False
    return True
      
      
  @staticmethod
  def addMenuUI(ldata = None, labelle: str = '', description: str = '', quantity: int = 0, price: float = 0.0, action = ''):
    """ @function shall return => p = add price; q = modify price; qp = both """
    global data
    print('''add''')
    if ldata != None:
      data = ldata
    if data.existsLabelle(labelle):
      if action=='':
        raise Exception('maaan coome on')
     
      match (action):
        case ('q'):
          if(quantity == 0):
            raise Exception("quantity to add shall not be 0")
          data.addQuantityByLabelle(labelle, quantity)
          print(f'the item with name : {labelle} got an addition in quantity by {quantity}')
          return
        case ('p'):
          if(price == 0.0):
            raise Exception("price shall not be 0")
          data.modifyColByLabelle(labelle, 'price', price)
          print(f'the item\'s new price = {price}')
          return
        case ('qp'):
          if(quantity == 0):
            raise Exception("quantity to add shall not be 0")
          if(price == 0.0):
            raise Exception("price shall not be 0")
          data.addQuantityByLabelle(labelle, quantity)
          print(f'the item with name : {labelle} got an addition in quantity by {quantity}')
          data.modifyColByLabelle(labelle, 'price', price)
          print(f'the item\'s new price = {price}')
          return
        case _:
          raise Exception('action should not be different than p, q, qp')
      
    data.insert(labelle, description, quantity, price)



  @staticmethod
  def expandQuantityMenu():
    '''add quantity'''
    print('''add quantity''')
    menu = int(input(DataAdder.msgaddstock))
    match (menu):
      case (1):
        print('''ref''')
        ref = int(input("enter the ref id to add item's quantity"))
        data.existsRef(ref)

        quantity = int(input("enter the quantity to add"))
        data.addQuantityByRef(ref, quantity)
      case (2):
        print('''labelle''')
        labelle = input("Enter the labelle to add item's quantity")
        data.existsLabelle(labelle)

        quantity = int(input("enter the quantity to add"))
        data.addQuantityByLabelle(labelle, quantity)
      case (0):
        return
    
class DataModder:
  msgmodify: str = '''
        1 - byRef
        2 - byLabelle
        3 - labelle(exp)
        4 - description(exp)
        5 - quantity(exp)
        6 - price(exp)
        0 - back
  '''
  msgmodifyBy: str = '''
            1 - byRef
            2 - byLabelle
            0 - back
  '''
  @staticmethod
  def modifyMenu():
    print('''modify''')
    menu = int(input(DataModder.msgmodify))
    match (menu):
        case (1):
            print('''modByRef''')
            ref = int(input('enter ref med to modify'))
            if data.existsRef(ref):
              labelle = input('Enter labelle')
              description = input('Enter description')
              quantity = int(input('Enter quantity'))
              price = float(input('Enter price'))
              data.modifyAllByRef(ref, labelle, description, quantity, price)
            else:
              print(f'ref : {ref} is not found!')
              
        case (2):
            print('''modByLabelle''')
            oldLabel = input('enter labelle med to modify')
            print(f"waaa3ibadllah {oldLabel}")
            if data.existsLabelle(oldLabel):
              labelle = input('Enter new labelle')
              description = input('Enter description')
              quantity = int(input('Enter quantity'))
              price = float(input('Enter price'))
              data.modifyAllByLabelle(oldLabel, labelle, description, quantity, price)
            else:
              print(f'label : {oldLabel} is not found!')
            
        case (3):
            print('''modLabelle (experimental)''')
            temp = DataModder.msgmodify.split('\n')[3]
            menu = int(input(temp + DataModder.msgmodifyBy))
            match (menu):
              case (1):
                print('''modLabelByRef''')
                ref = int(input('enter ref med to modify'))
                if data.existsRef(ref):
                  labelle = input('Enter new labelle')
                  data.modifyColByRef(ref, 'labelle', labelle)
                else:
                  print(f'ref : {ref} is not found!')
                  
              case (2):
                print('''modLabelByLabel''')
                oldLabelle = input('Enter labelle')
                if data.existsLabelle(oldLabelle):
                  labelle = input('Enter new labelle')
                  data.modifyColByLabelle(oldLabelle, 'labelle', labelle)
                else:
                  print(f'label : {oldLabelle} is not found!')
              case (0):
                return
                  
        case (4):
            print('''modDescription (experimental)''')
            temp = DataModder.msgmodify.split('\n')[4]
            menu = int(input(temp + DataModder.msgmodifyBy))
            match (menu):
              case (1):
                print('''modDescriptionByRef''')
                ref = int(input('enter ref med to modify'))
                if data.existsRef(ref):
                  Description = input('Enter new Description')
                  data.modifyColByRef(ref, 'Description', Description)
                else:
                  print(f'ref : {ref} is not found!')
                  
              case (2):
                print('''modDescriptionByLabel''')
                oldLabelle = input('Enter labelle')
                if data.existsLabelle(oldLabelle):
                  Description = input('Enter new Description')
                  data.modifyColByLabelle(oldLabelle, 'Description', Description)
                else:
                  print(f'label : {oldLabelle} is not found!')  
              case (0):
                return
                  
        case (5):
            print('''modquantity (experimental)''')
            temp = DataModder.msgmodify.split('\n')[5]
            menu = int(input(temp + DataModder.msgmodifyBy))
            match (menu):
              case (1):
                print('''modquantityByRef''')
                ref = int(input('enter ref med to modify'))
                if data.existsRef(ref):
                  quantity = input('Enter new quantity')
                  data.modifyColByRef(ref, 'quantity', quantity)
                else:
                  print(f'ref : {ref} is not found!')
                  
              case (2):
                print('''modquantityByLabel''')
                oldLabelle = input('Enter labelle')
                if data.existsLabelle(oldLabelle):
                  quantity = input('Enter new quantity')
                  data.modifyColByLabelle(oldLabelle, 'quantity', quantity)
                else:
                  print(f'label : {oldLabelle} is not found!')
              case (0):
                return
        case (6):
            print('''modprice (experimental)''')
            temp = DataModder.msgmodify.split('\n')[6]
            menu = int(input(temp + DataModder.msgmodifyBy))
            match (menu):
              case (1):
                print('''modpriceByRef''')
                ref = int(input('enter ref med to modify'))
                if data.existsRef(ref):
                  price = input('Enter new price')
                  data.modifyColByRef(ref, 'price', price)
                else:
                  print(f'ref : {ref} is not found!')
                  
              case (2):
                print('''modpriceByLabel''')
                oldLabelle = input('Enter labelle')
                if data.existsLabelle(oldLabelle):
                  price = input('Enter new price')
                  data.modifyColByLabelle(oldLabelle, 'price', price)
                else:
                  print(f'label : {oldLabelle} is not found!')
              case (0):
                return
          
          
        case (0):
          return
        
class DataFinder:
  msgsearch: str = '''
        1 - ref
        2 - labelle
        3 - labelle(contain)
        0 - back
  '''
  @staticmethod
  def searchMenu():
    print('''search''')
    menu = int(input(DataFinder.msgsearch))
    match (menu):
        case (1):
            print('''ref''')
            ref = int(input('enter the ref id to search and show item'))
            print(data.getRef(ref))
        case (2):
            print('''labelle''')
            labelle = input('Enter the labelle to search and show item')
            print(data.getLabelle(labelle))
        case (3):
            print('''labelle(contain)''')
            labelle = input('Enter the labelle or sublabelle to search and show item')
            print(data.getLabelleContain(labelle))
        case (0):
          return

class DataRemover:
  msgremove: str = '''
        1 - all
        2 - ref
        3 - labelle
        0 - back
  '''
  msgconsume: str = '''
        1 - ref
        2 - labelle
        0 - back
  '''
  @staticmethod
  def removeMenu():
    print('''remove''')
    menu = int(input(DataRemover.msgremove))
    match (menu):
      case (1):
        print('''all''')
        data.removeAll()
      case (2):
        print('''ref''')
        ref = int(input('enter the ref id to remove item'))
        data.removeByRef(ref)
      case (3):
        print('''labelle''')
        labelle = input('Enter the labelle to remove item')
        data.removeByLabelle(labelle)
      case (0):
        return
      
  @staticmethod
  def consumeQuantityMenu():
    print('''consume quantity''')
    menu = int(input(DataRemover.msgconsume))
    match (menu):
      case (1):
        print('''ref''')
        ref = int(input('enter the ref id to consume item'))
        if data.existsRef(ref):
          quantity = int(input('enter the quantity to consume'))
          data.consumeByRef(ref, quantity)
        else:
          print(f'ref : {ref} is not found!')

      case (2):
        print('''labelle''')
        labelle = input('Enter the labelle to consume item')
        if data.existsLabelle(labelle):
          quantity = int(input('enter the quantity to consume'))
          data.consumeByLabelle(labelle, quantity)
        else:
          print(f'label : {labelle} is not found!')
      case (0):
        return
        


if __name__ == '__main__':
  data = RDB('data/MedStocks.db')
  data.createTable()
  data.save()
  
  # data.insert("Nothing", "I said it is nothing", 0, 0.0)
  # data.modifyRef(5, "fifth one modified", "Nodesc yet", 69, 6969)
  print(data.getColumnName())



  msg: str = '''
      1 - show        
      2 - add med    
      3 - modify med        
      4 - search        
      5 - remove    
      6 - consume quantity
      7 - add quantity
      0 - exit
  '''

  menu: int = -1
  while (menu != 0):
    try:
      menu = int(input(msg))
      match(menu):
        case (1):
          DataShower.showMenu()
        case (2):
          DataAdder.addMenu()
        case (3):
          DataModder.modifyMenu()
        case (4):
          DataFinder.searchMenu()
        case (5):
          DataRemover.removeMenu()
        case (6):
          DataRemover.consumeQuantityMenu()
        case (7):
          DataAdder.expandQuantityMenu()
    except ValueError:
      print("The input is not an integer type")
      menu = -1
    finally:
      if menu == -1 or menu > 7 or menu < 0:
        print("only numbers between 0 and 7 are allowed")

# data.printData('*')
# cursor.execute(f"INSERT INTO stocks\
#                VALUES ( 2, 'Supradine', 'vitamines', 100, 37.5)")

# data.database.commit()
# cursor.execute(create_table)


# cursor.execute('SELECT * FROM stocks')
# for item in cursor.fetchall():
#     print(item)
# result = data.getColumnName()
#
# columns = []
# for head in result:
#   r =str(head)
#   columns.append(r)
# columns = tuple(columns)
#
# print(columns)
