
from file import *
from JS import *

msg1 = '''

    1 - Insert an item
    2 - Remove an item
    3 - Modify an item
    4 - Show/Read items

'''

choice = 0

if __name__ == '__main__':
    DataRef = DataManager()
    while True:
        Info(msg1)
        choice = int(input("Insert your choice"))
        match choice:
            case 1:
                tempName = input("Insert the name of the new med")
                tempPrice = float(input("Insert the price of the new med"))
                tempQuantity = int(input("Insert the quantity of the new med"))
                DataRef.AddItemToFile(tempName, tempPrice, tempQuantity)
            case 2:
                tempName = input("Insert the name of the new med")
                DataRef.RemoveItemByName(tempName)
            case 3:
                tempId = int(input("Insert the id of the med"))
                tempName = input("Insert the new name of the med")
                tempPrice = float(input("Insert the new price of the med"))
                tempQuantity = int(input("Insert the new quantity of the med"))
                DataRef.ModifyById(tempId, tempName, tempPrice, tempQuantity)
            case 4:
                DataRef.ReadItems()
            case _:
                Error("Choose again :)")

        if(choice == 5):
            break

    # 
    
    # D.ReadItems()
    # D.AddItemToFile("Dol", 20, 300)
    # D.AddItemToFile("DP", 250, 30)
    # D.RemoveItemByName("DP")

  