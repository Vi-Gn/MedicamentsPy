from file import *
from ItemMeds import *


class DataEntry:
    def __init__(self, Path):
        self.Path = Path
        self.FileRef = File(Path)
        self.DataArray = []

    def __del__(self):        
        self.FileRef.Close()
        
    def FindId(self, Medicament):
        
