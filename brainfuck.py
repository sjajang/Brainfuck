import sys, bf

def execute(file):
    try:
        f = open(file, 'r')
        bf.execute(f.read())
        f.close()
    except FileNotFoundError:
        print("Error: File Not Found")

def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        print('Usage: brainfuck.py [filename]')

if __name__ == "__main__":
    main()
