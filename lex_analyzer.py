def lexAnalyze(tokens): # fungsi untuk melakukan analisis leksikal
    transition_table = {}  

    #Transisi if -> variabel
    transition_table[('q0', 'if')] = 'q1'
    transition_table[('q1', ' ')] = 'q2'
    transition_table[('q2', ' ')] = 'q2'

    #Transisi variabel - operator
    transition_table[('q2', 'a')] = 'q3'
    transition_table[('q2', 'b')] = 'q3'
    transition_table[('q2', 'c')] = 'q3'
    transition_table[('q2', 'd')] = 'q3'
    transition_table[('q2', 'e')] = 'q3'
    transition_table[('q3', ' ')] = 'q3'

    transition_table[('q3', '==')] = 'q4'
    transition_table[('q3', '<=')] = 'q4'
    transition_table[('q3', '>=')] = 'q4'
    transition_table[('q3', '>')] = 'q4'
    transition_table[('q3', '<')] = 'q4'
    transition_table[('q4', ' ')] = 'q4'

    #Transisi operator ke variabel
    transition_table[('q4', 'a')] = 'q5'
    transition_table[('q4', 'b')] = 'q5'
    transition_table[('q4', 'c')] = 'q5'
    transition_table[('q4', 'd')] = 'q5'
    transition_table[('q4', 'e')] = 'q5'
    transition_table[('q5', ' ')] = 'q5'

    #Transisi jika ada operator && dan ||
    transition_table[('q5', '&&')] = 'q2'
    transition_table[('q5', '||')] = 'q2'

    #Transisi masuk ke dalam aksi
    transition_table[('q5', '{')] = 'q6'
    transition_table[('q6', ' ')] = 'q6'

    #Transisi variabel aksi
    transition_table[('q6', 'a')] = 'q7'
    transition_table[('q6', 'b')] = 'q7'
    transition_table[('q6', 'c')] = 'q7'
    transition_table[('q6', 'd')] = 'q7'
    transition_table[('q6', 'e')] = 'q7'
    transition_table[('q7', ' ')] = 'q7'

    #Transisi operator aksi
    transition_table[('q7', '=')] = 'q8'
    transition_table[('q8', ' ')] = 'q8'

    #Transisi jika variabel aksi lagi
    transition_table[('q8', 'a')] = 'q9'
    transition_table[('q8', 'b')] = 'q9'
    transition_table[('q8', 'c')] = 'q9'
    transition_table[('q8', 'd')] = 'q9'
    transition_table[('q8', 'e')] = 'q9'
    #angka
    transition_table[('q8', '1')] = 'q9'
    transition_table[('q8', '2')] = 'q9'
    transition_table[('q8', '3')] = 'q9'
    transition_table[('q8', '3')] = 'q9'
    transition_table[('q8', '5')] = 'q9'
    transition_table[('q9', ' ')] = 'q9'

    #Transisi jika ada operator kalkulasi
    transition_table[('q9', '+')] = 'q8'
    transition_table[('q9', '-')] = 'q8'
    transition_table[('q9', '/')] = 'q8'
    transition_table[('q9', '*')] = 'q8'

    #Transisi keluar dari aksi
    transition_table[('q9', '}')] = 'q10'
    transition_table[('q10', ' ')] = 'q10'
    transition_table[('q10', '#')] = 'accept'

    #Transisi jika ada else
    transition_table[('q10', 'else')] = 'q11'
    transition_table[('q11', ' ')] = 'q11'

    #Transisi masuk aksi else
    transition_table[('q11', '{')] = 'q12'
    transition_table[('q12', ' ')] = 'q12'

    #Transisi masuk variabel aksi else
    transition_table[('q12', 'a')] = 'q13'
    transition_table[('q12', 'b')] = 'q13'
    transition_table[('q12', 'c')] = 'q13'
    transition_table[('q12', 'd')] = 'q13'
    transition_table[('q12', 'e')] = 'q13'
    transition_table[('q13', ' ')] = 'q13'

    #Transisi masuk operator aksi else
    transition_table[('q13', '=')] = 'q14'
    transition_table[('q14', ' ')] = 'q14'

    #Transisi jika variabel aksi lagi
    transition_table[('q14', 'a')] = 'q15'
    transition_table[('q14', 'b')] = 'q15'
    transition_table[('q14', 'c')] = 'q15'
    transition_table[('q14', 'd')] = 'q15'
    transition_table[('q14', 'e')] = 'q15'
    #angka
    transition_table[('q14', '1')] = 'q15'
    transition_table[('q14', '2')] = 'q15'
    transition_table[('q14', '3')] = 'q15'
    transition_table[('q14', '3')] = 'q15'
    transition_table[('q14', '5')] = 'q15'
    transition_table[('q15', ' ')] = 'q15'

    #Transisi jika ada operator kalkulasi
    transition_table[('q15', '+')] = 'q14'
    transition_table[('q15', '-')] = 'q14'
    transition_table[('q15', '/')] = 'q14'
    transition_table[('q15', '*')] = 'q14'

    #Transisi keluar dari aksi else
    transition_table[('q15', '}')] = 'q16'
    transition_table[('q16', ' ')] = 'q16'
    transition_table[('q16', '#')] = 'accept'
    
    print('\nState yang dilewati:') # Output state yang dilewati
    currentState = 'q0' # inisialisasi state awal
    for token in tokens: # looping token
        try: 
            currentState = transition_table[currentState, token] # mencari state berikutnya
        except:
            break
        print(currentState) #output state yang dilewati

    if currentState == 'accept': # cek apakah state terakhir adalah accept
        print('\nSeleksi kondisi If-Else pada Golang valid') # jika ya, valid
    else:
        print(f'\nSeleksi kondisi If-Else pada Golang tidak valid, transisi pada {currentState} gagal') # jika tidak, tidak valid