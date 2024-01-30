
from file import *
from JS import *



if __name__ == '__main__':
    # file = open("JSON.json", "w+")
    # D = { "Meds": [ { "id": 1, "name": "doliprane", "Price": 20, "Quantity": 150 }, 
    #                 { "id": 2, "name": "Aspro", "Price": 15, "Quantity": 90 }, 
    #                 { "id": 3, "name": "Supradine", "Price": 36, "Quantity": 250 }]}
    # json.dump(D,file,indent=4)
    # file.close()
    D = DataManager()
    D.AddItemToFile("Dol", 20, 300)
    D.AddItemToFile("DP", 250, 30)
    D.RemoveItemByName("DP")

    # F = File("Database/MedicsData.txt")
    # # F.WriteLineAppend("dsd")

    # print(F.ReadLine(),end = "")
    # print(F.ReadLine(),end = "")
    # print(F.ReadLine(),end = "")
    # print(F.ReadLine(),end = "")
    # print(F.ReadLine(),end = "")
    # print(F.ReadLine(),end = "")
    # print(F.ReadLine(),end = "")
    # print(F.ReadLine(),end = "")

    # file = open("JSON.json", "w+")
    # D = { "Meds": [ { "id": 1, "name": "doliprane", "Price": 20, "Quantity": 150 }, 
    #                 { "id": 2, "name": "Aspro", "Price": 15, "Quantity": 90 }, 
    #                 { "id": 3, "name": "Supradine", "Price": 36, "Quantity": 250 }]}
    # json.dump(D,file,indent=4)
    # file.close()

    