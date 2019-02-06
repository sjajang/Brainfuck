# Brainfuck Programming Language
# Author: Sanjangeet Singh Jajang
# --------------------------------------------

import sys

def getch():
    
    try:
        
        # Windows
        import msvcrt
        return msvcrt.getch()
    
    except ImportError:
        
        # Unix
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            
        return ch

def _build_map(code):
    temp, _map = [], {}
    
    for pos, cmd in enumerate(code):
        if cmd == "[": temp.append(pos)
        if cmd == "]":
            start = temp.pop()
            _map[start] = pos
            _map[pos] = start
            
    return _map

# -----------------------------------------------------------------
# > : increment the data pointer
# < : decrement the data pointer
# + : increment the byte at the data pointer
# - : decrement the byte at the data pointer
# . : output the byte at the data pointer
# , : accept one byte of input, storing its value in the byte at
#     the data pointer
# [ : if the byte at the data pointer is zero, then instead of
#     moving the instruction pointer forward to the next command,
#     jump it forward to the command after the matching ] command. 
# ] : if the byte at the data pointer is nonzero, then instead of
#     moving the instruction pointer forward to the next command,
#     jump it back to the command after the matching [ command.
# -----------------------------------------------------------------

def evaluate(code):
    code = ''.join(filter(lambda x: x in ['.',',','[',']','+','-','<','>'], list(code)))
    _map = _build_map(code)
    
    mat, ptr, codeptr = [0], 0, 0
    
    while codeptr < len(code):
        cmd = code[codeptr]
        
        if cmd == ">":
            ptr += 1
            if ptr == len(mat): mat.append(0)
        if cmd == "<":
            ptr = 0 if ptr <=0 else ptr - 1
            
        if cmd == "+":
            mat[ptr] = mat[ptr] + 1 if mat[ptr] < 255 else 0
        if cmd == "-":
            mat[ptr] = mat[ptr] - 1 if mat[ptr] > 0 else 255
            
        if cmd == "[" and mat[ptr] == 0: codeptr = _map[codeptr]
        if cmd == "]" and mat[ptr] != 0: codeptr = _map[codeptr]
        
        if cmd == ".": sys.stdout.write(chr(mat[ptr]))
        if cmd == ",": mat[ptr] = ord(getch())
        
        codeptr +=1

def execute(code):
    evaluate(code)
