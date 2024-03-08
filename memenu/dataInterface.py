class DataInterface:
  @staticmethod
  def GetDataLists(data):
    """this returns a list of items and each list has a list of cols"""
    DataGetter.showAll()
  
  
  
  

class DataGetter:
  
  @staticmethod
  def getAll(dataRef):
    return dataRef.getData('*')
         
  @staticmethod
  def getlabelle(dataRef):
    return dataRef.getData('labelle')
           
  @staticmethod
  def getDescription(dataRef):
    return dataRef.getData('description')
      
  @staticmethod
  def getQuantity(dataRef):
    return dataRef.getData('quantity')

  @staticmethod
  def getPrice(dataRef):
    return dataRef.getData('price')
      

    
class DataAdder:
  @staticmethod
  def addMenu(dataRef):
    print('''add''')
    labelle = input('Enter labelle')
    description = input('Enter description')
    quantity = int(input('Enter quantity'))
    price = float(input('Enter price'))
    dataRef.insert(labelle, description, quantity, price)
    
  @staticmethod
  def expandQuantityMenu(dataRef):
    print('''add quantity''')
    menu = int(input(DataAdder.msgaddstock))
    match (menu):
      case (1):
        print('''ref''')
        ref = int(input("enter the ref id to add item's quantity"))
        dataRef.existsRef(ref)

        quantity = int(input("enter the quantity to add"))
        dataRef.addQuantityByRef(ref, quantity)
      case (2):
        print('''labelle''')
        labelle = input("Enter the labelle to add item's quantity")
        dataRef.existsLabelle(labelle)

        quantity = int(input("enter the quantity to add"))
        dataRef.addQuantityByLabelle(labelle, quantity)
    
    
class DataModder:
  msgmodify: str = '''
        1 - ref
        2 - labelle
  '''
  @staticmethod
  def modifyMenu(dataRef):
    print('''modify''')
    menu = int(input(DataModder.msgmodify))
    match (menu):
        case (1):
            print('''ref''')
            ref = int(input('enter ref med to modify'))
            dataRef.existsRef(ref)

            labelle = input('Enter labelle')
            description = input('Enter description')
            quantity = int(input('Enter quantity'))
            price = float(input('Enter price'))
            dataRef.modifyRef(ref, labelle, description, quantity, price)
        case (2):
            print('''labelle''')
            oldLabel = input('enter labelle med to modify')
            dataRef.existsLabelle(oldLabel)

            labelle = input('Enter new labelle')
            description = input('Enter description')
            quantity = int(input('Enter quantity'))
            price = float(input('Enter price'))
            dataRef.modifyLabelle(oldLabel, labelle, description, quantity, price)

    
class DataFinder:
  msgsearch: str = '''
        1 - ref
        2 - labelle
        3 - labelle(contain)
  '''
  @staticmethod
  def searchMenu(dataRef):
    print('''search''')
    menu = int(input(DataFinder.msgsearch))
    match (menu):
        case (1):
            print('''ref''')
            ref = int(input('enter the ref id to search and show item'))
            print(dataRef.getRef(ref))
        case (2):
            print('''labelle''')
            labelle = input('Enter the labelle to search and show item')
            print(dataRef.getLabelle(labelle))
        case (3):
            print('''labelle(contain)''')
            labelle = input('Enter the labelle or sublabelle to search and show item')
            print(dataRef.getLabelleContain(labelle))


class DataRemover:
  msgremove: str = '''
        1 - all
        2 - ref
        3 - labelle
  '''
  @staticmethod
  def removeMenu(dataRef):
    print('''remove''')
    menu = int(input(DataRemover.msgremove))
    match (menu):
      case (1):
        print('''all''')
        dataRef.removeAll()
      case (2):
        print('''ref''')
        ref = int(input('enter the ref id to remove item'))
        dataRef.removeByRef(ref)
      case (3):
        print('''labelle''')
        labelle = input('Enter the labelle to remove item')
        dataRef.removeByLabelle(labelle)
        
  @staticmethod
  def consumeQuantityMenu(dataRef):
    print('''consume quantity''')
    menu = int(input(DataRemover.msgremove))
    match (menu):
      case (1):
        print('''ref''')
        ref = int(input('enter the ref id to consume item'))
        dataRef.existsRef(ref)

        quantity = int(input('enter the quantity to consume'))
        dataRef.consumeByRef(ref, quantity)
      case (2):
        print('''labelle''')
        labelle = input('Enter the labelle to consume item')
        dataRef.existsLabelle(labelle)

        quantity = int(input('enter the quantity to consume'))
        dataRef.consumeByLabelle(labelle, quantity)
        
        