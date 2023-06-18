from parser_1 import parse
from lex_analyzer import lexAnalyze

def main():
    tokens = []
    with open('input.txt') as f:
        lines = f.readlines()
        lines = ''.join(lines)
        tokens = parse(lines)
     
    print("\n".join(tokens[0]))
    lexAnalyze(tokens[0])

if __name__ == "__main__":
    main()
