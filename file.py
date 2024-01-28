

class File:
    def __init__(self, Path: str):
        self.Path = Path
        self.FileRef = open(Path, "r")
        self.FileRef.close()

    def __del__(self):
        self.Close()
        
    def Open(self, Mode: str):
        if self.IsClosed():          
            self.FileRef = open(self.Path, Mode)
            print(f"The File in {self.Path} | Got Opened Successfully")
            return 
        
        elif self.GetMode() == Mode:
            print(f"The File in {self.Path} | Is Already Opened")
            return
          
        else: # elif self.GetMode() != Mode:
            temp = self.GetMode()
            self.Close()
            self.FileRef = open(self.Path, Mode)
            print(f"The File in {self.Path} | Got Opened Successfully Toggled From '{temp}' mode to '{Mode}'")

        
    def Close(self):
        if self.FileRef.closed:
            print(f"The File in {self.Path} | Is Already Closed")
            return 
        self.FileRef.close()
        print(f"The File in {self.Path} | Got Closed Successfully")
    
    
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
            print(f"Couldn't write to file in path {self.Path}")
   
    def WriteAppend(self, Data: str):
        self.Open("a")
        self.FileRef.write(Data)
        if not(self.IsWritable()):
            print(f"Couldn't write to file in path {self.Path}")
        
    def WriteLineOverride(self, Data: str):
        self.Open("w")
        self.FileRef.write(Data + "\n")
        if not(self.IsWritable()):
            print(f"Couldn't write to file in path {self.Path}")
   
    def WriteLineAppend(self, Data: str):
        self.Open("a")
        self.FileRef.write(Data + "\n")
        if not(self.IsWritable()):
            print(f"Couldn't write to file in path {self.Path}")
        
        
    
    def Read(self):
        self.Open("r")
        return self.FileRef.read()
    
    def ReadLine(self) -> str:
        self.Open("r")
        temp = self.FileRef.readline()
        if temp == "":
            return "heelp"
        return temp


