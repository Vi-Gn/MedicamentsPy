from Log import *

class File:
    def __init__(self, Path: str, DebugMode : bool = False):
        self.Path = Path
        self.FileRef = open(Path, "r")
        self.FileRef.close()
        self.DebugMode = DebugMode
        if(self.DebugMode):
            Warn("File is running debug mode.")

    def __del__(self):
        self.Close()
        
    def Open(self, Mode: str):
        if self.IsClosed():          
            self.FileRef = open(self.Path, Mode)
            if(self.DebugMode):
                Info(f"The File in {self.Path} | Got Opened Successfully")
            return 
        
        elif self.GetMode() == Mode:
            if(self.DebugMode):
                Info(f"The File in {self.Path} | Is Already Opened")
            return
          
        else: # elif self.GetMode() != Mode:
            temp = self.GetMode()
            self.Close()
            self.FileRef = open(self.Path, Mode)
            if(self.DebugMode):
                Info(f"The File in {self.Path} | Got Opened Successfully Toggled From '{temp}' mode to '{Mode}'")

        
    def Close(self):
        if self.FileRef.closed:
            if(self.DebugMode):
                Info(f"The File in {self.Path} | Is Already Closed")
            return 
        self.FileRef.close()
        if(self.DebugMode):
            Info(f"The File in {self.Path} | Got Closed Successfully")
    
    
    def IsClosed(self):
        return self.FileRef.closed            
        
    def ChangePath(self, Path: str):
        self.Close()
        self.Path = Path

    def IsReadable(self):
        return self.FileRef.readable()
    
    def IsWritable(self):
        return self.FileRef.writable()

    def GetMode(self):
        return self.FileRef.mode

    def WriteOverride(self, Data: str):
        self.Open("w")
        self.FileRef.write(Data)
        if not(self.IsWritable()):
            Error(f"Couldn't write to file in path {self.Path}")
   
    def WriteAppend(self, Data: str):
        self.Open("a")
        self.FileRef.write(Data)
        if not(self.IsWritable()):
            Error(f"Couldn't write to file in path {self.Path}")
        
    def WriteLineOverride(self, Data: str):
        self.Open("w")
        self.FileRef.write(Data + "\n")
        if not(self.IsWritable()):
            Error(f"Couldn't write to file in path {self.Path}")
   
    def WriteLineAppend(self, Data: str):
        self.Open("a")
        self.FileRef.write(Data + "\n")
        if not(self.IsWritable()):
            Error(f"Couldn't write to file in path {self.Path}")
        
        
    def Read(self):
        self.Open("r")
        return self.FileRef.read()
    
    def ReadLine(self, log: bool = False) -> str:
        self.Open("r")
        temp = self.FileRef.readline()
        if temp == "":
            Warn("This file has reached the end line")
        if log:
            Log(temp, end="")
        return temp

    
