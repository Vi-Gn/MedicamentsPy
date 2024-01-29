
def Info(msg: str = ""):
    print("\n\nInfos   : " + msg + "\n")

def Trace(msg: str = ""):
    print("\n\nTraces  : " + msg + "\n")

def Warning(msg: str = ""):
    print("\n\nWarning : " + msg + "\n")

def Error(msg: str = ""):
    print("\n\nErrors  : " + msg + "\n")

def Fatal(msg: str = ""):
    print("\n\nFatals  : " + msg + "\n")

def Log(msg: str = "", willBreakLine: str = "\n"):
    print("\n\n          " + msg, end = willBreakLine)