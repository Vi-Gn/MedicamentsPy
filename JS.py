import json

D = { "id": 1, "name": "doliprane", "Price": 20, "Quantity": 150 }
class DataManager:
    def __init__(self, Path: str = "JSON.json"):
        self.Path = Path
        self.Data = {}
        self.File = open(Path, "r")
        self.File.close()

    def __del__(self):
        self.File.close()

    def GetData(self, KeyName: str = "Meds") -> dict:
        DataDict = { KeyName: []}
        self.File = open(self.Path, "r")
        fileLength = len(self.File.read())
        self.File.seek(0)
        if ( fileLength != 0):
            DataDict = json.load(self.File)
        self.File.close()
        return DataDict

    # def GetDataArray(self, KeyName: str = "Meds") -> list:
    #     Currentdata = self.GetData()
    #     DataArray = list(Currentdata[KeyName])
    #     return DataArray
    
    def AddItemToFile(self, MedName: str, MedPrice: float, MedQuantity: int,  KeyName: str = "Meds"):
        Currentdata = self.GetData()
        count = len(Currentdata[KeyName])
        if count == 0:
            Id = 1
        else:
            Id = count + 1
        Currentdata[KeyName].append({ "id": Id, "name": MedName, "Price": MedPrice, "Quantity": MedQuantity })
        self.File = open(self.Path, "w")
        json.dump(Currentdata, self.File, indent=4)
        self.File.close()
        

    def RemoveItemByName(self, MedName: str,  KeyName: str = "Meds"):
        Currentdata = self.GetData()
        count = len(Currentdata[KeyName])
        if count == 0:
            return False
        else:
            for i in range(count):
                if MedName in Currentdata[KeyName][i]["name"]:
                    del Currentdata[KeyName][i]
                    self.File = open(self.Path, "w")
                    json.dump(Currentdata, self.File, indent=4)
                    self.File.close()
