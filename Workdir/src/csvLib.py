import csv

StructMeds = {'id': -1, 'name': "None", 'quantity': -1, 'price': -1}



def GetLastIndex(path: str = 'data.csv'):
  with open(path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    Med = list(csv_reader)
    return Med[-1]['id']

def ReadCSV(path: str = 'data.csv'):
  with open(path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    Med = list(csv_reader)
    return Med




def PrintCSV(path: str = 'data.csv'):
  with open(path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
      print(line)

def FindMedByName(name: str, path: str = 'data.csv'):
  with open(path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
      if line['name'] == name:
        return True
      
  return False

def AddRow(name: str, quantity: int, price:float):
  if FindMedByName(name):
    print("Med Name Already In List")
    return False

  with open('data.csv', 'a', newline='') as csv_file:
    fieldnames = list(StructMeds.keys())
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    Med = StructMeds.copy()

    Med['id'] = int(GetLastIndex()) + 1
    Med['name'] = name
    Med['quantity'] = quantity
    Med['price'] = price
    print(Med)
    csv_writer.writerow(Med)
  return True

def ModifyId(index: int, name: str ='', quantity: int = -1, price: int = -1):
  """ first index is 1 """
  if index < 1:
    print("Operation failed! : Fisrt Index Is 1")
  else:
    with open('data.csv', 'a+', newline='') as csv_file:
      csv_file.seek(0)
      csv_reader = csv.DictReader(csv_file)
      Med = list(csv_reader)
      
      for i in range(len(Med)):
        if Med[i]['id'] == str(index):
          
          if (name != ''):
            Med[i]['name'] = name

          if (price != -1):
            Med[i]['price'] = price

          if (quantity != -1):
            Med[i]['quantity'] = quantity
      
      Med.append(StructMeds)

      with open('data.csv', 'w', newline='') as write_csv_file:

        fieldnames = list(StructMeds.keys())

        csv_writer = csv.DictWriter(write_csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        for line in Med:
          if int(line['id']) >= 1:
            csv_writer.writerow(line)
            

def Row(index: int = 1):
  """ first index is 1 """
  if index < 1:
    print("Operation failed! : Fisrt Index Is 1")
  else:
    return ReadCSV()[index - 1]
          
def RowList(index: int = 0):
  if index < 1:
    print("Operation failed! : Fisrt Index Is 1")
  else:
    return list(Row(index).values())

# print(GetLastIndex())
# print(RowList(1))
# AddRow(name="bttikh", quantity=20, price=46)
# PrintCSV()
# ModifyId(1, quantity=400)

    