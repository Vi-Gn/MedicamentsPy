
def Info(msg: str = ""):
    print("\x1b[36m" + "\nInfos   : " + msg + "\n" + "\x1b[0m")

def Trace(msg: str = ""):
    print("\x1b[32m" + "\nTraces  : " + msg + "\n" + "\x1b[0m")

def Warn(msg: str = ""):
    print("\x1b[33m" + "\nWarning : " + msg + "\n" + "\x1b[0m")

def Error(msg: str = ""):
    print("\x1b[31m" + "\nErrors  : " + msg + "\n" + "\x1b[0m")

def Fatal(msg: str = ""):
    print("\x1b[35m" + "\nFatals  : " + msg + "\n" + "\x1b[0m")
    exit(code=5)

def Log(msg: str, R: int = 255, G: int = 255, B: int = 255, willBreakLine: str = "\n"):
    print(f"\x1b[38;2;{R};{G};{B}m" + "\n          " + msg, end = willBreakLine + "\x1b[0m")

def Input(msg: str = "", R: int = 255, G: int = 255, B: int = 255, willBreakLine: str = "\n"):
    print(f"\x1b[38;2;{R};{G};{B}m" + "\n          " + msg, end = willBreakLine + "\x1b[0m")
    return input()


if __name__ == '__main__':
    Info("this is info")
    Trace("this is trace")
    Warn("this is Warning")
    Error("this is error")
    Fatal("this is fatal")
    Log(msg = "this is Log", R = 150, G = 20,B = 20)

