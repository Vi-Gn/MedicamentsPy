
def Info(msg: str = ""):
    print("\x1b[36m" + "\n\nInfos   : " + msg + "\n" + "\x1b[0m")

def Trace(msg: str = ""):
    print("\x1b[32m" + "\n\nTraces  : " + msg + "\n" + msg + "\n" + "\x1b[0m")

def Warn(msg: str = ""):
    print("\x1b[33m" + "\n\nWarning : " + msg + "\n" + "\x1b[0m")

def Error(msg: str = ""):
    print("\x1b[31m" + "\n\nErrors  : " + msg + "\n" + "\x1b[0m")

def Fatal(msg: str = ""):
    print("\x1b[35m" + "\n\nFatals  : " + msg + "\n" + "\x1b[0m")

def Log(msg: str, R: int = 255, G: int = 255, B: int = 255, willBreakLine: str = "\n"):
    print(f"\x1b[38;2;{R};{G};{B}m" + "\n\n          " + msg, end = willBreakLine + "\x1b[0m")

def Input(msg: str = "", R: int = 255, G: int = 255, B: int = 255, willBreakLine: str = "\n"):
    print(f"\x1b[38;2;{R};{G};{B}m" + "\n\n          " + msg, end = willBreakLine + "\x1b[0m")
    return input()