from file import *
from ItemMeds import *


class DataEntry:
    def __init__(self, Path: str):
        self.Path = Path
        self.FileRef = File(Path)
        self.DataArray = []

    def __del__(self):        
        self.FileRef.Close()
    
    def Open(self, Mode: str):
        self.FileRef.Open(Mode)

    def FindId(self, Id: int):
        self.Open("r")
        for i in range()
        self.FileRef.ReadLine()
