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

    def GetData(self) -> dict:
        self.File = open(self.Path, "r")
        print(len(self.File.read()))
        self.File.seek(0)
        DataDict = json.load(self.File)
        self.File.close()
        return DataDict

    def GetDataArray(self, KeyName: str = "Meds") -> list:
        Currentdata = self.GetData()
        DataArray = list(Currentdata[KeyName])
        return DataArray
    
    def AddItemToFile(self, MedName: str, MedPrice: float, MedQuantity: int,  KeyName: str = "Meds"):
        Currentdata = self.GetData()
        CurrentdataArray = Currentdata[KeyName]
        count = len(CurrentdataArray)
        if count == 0:
            Id = 0
        else:
            Id = count
        
        Currentdata[KeyName].append({ "id": Id, "name": MedName, "Price": MedPrice, "Quantity": MedQuantity })
        print(Currentdata[KeyName])
        # self.File = open(self.Path, "w")
        # json.dump(Currentdata, self.File, indent=4)
        # self.File.close()
        # NewData = json.load(file)
        # tempData = tempDataFile["Meds"]
        # tempData.append({ "id": 4, "name": "doli", "Price": 18, "Quantity": 50 })
        # json.dump(Data,file,indent=4)
        # file.close()


    def LoadItemsFromFile(Path: str):
        file = open(Path, "r")
        data = json.load(file)
        medData = data["Meds"]
        medData.append({ "id": 4, "name": "doli", "Price": 18, "Quantity": 50 })
        # medData[]
        for med in medData:
            print(med)
        file.close()