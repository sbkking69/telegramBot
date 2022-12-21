from clases import *
from ctypes import *

def CursorPosition(x,y):
    print_at(x,y,'')


STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass

COORD._fields_ = [("X", c_short), ("Y", c_short)]

def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

    c = s.encode("cp866")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
