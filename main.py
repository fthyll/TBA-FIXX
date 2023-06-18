from parser_1 import parse # import fungsi parse dari parser_1.py
from lex_analyzer import lexAnalyze # import fungsi lexAnalyze dari lex_analyzer.py

def main(): 
    tokens = [] # daftar token yang sudah diurutkan
    with open('input.txt') as f: # membaca file input.txt
        lines = f.readlines() # membaca setiap baris
        lines = ''.join(lines) # menggabungkan setiap baris
        tokens = parse(lines) # memanggil fungsi parse
     
    print("\n".join(tokens[0])) # menampilkan token yang sudah diurutkan
    lexAnalyze(tokens[0]) # memanggil fungsi lexAnalyze

if __name__ == "__main__":
    main()
