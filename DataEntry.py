from file import *



# ID
# Name
# Price

class DataEntry:
    def __init__(self, Path):
        self.Path = Path
        self.FileRef = File(Path)
        self.DataArray = []

    def __del__(self):        
        self.FileRef.Close()
        
    def FindId(self):
