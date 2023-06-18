def parse(sentence):
    sentence = sentence.split('\n') # memisahkan setiap baris

    clean_sentence = [] # daftar token yang sudah dibersihkan
    for part in sentence: 
        clean_sentence.append(part.strip()) # membersihkan setiap baris
    clean_sentence = "".join(clean_sentence) # menggabungkan setiap baris

    ordered_token = [] # daftar token yang sudah diurutkan
    buffer = [] # buffer untuk menampung token
    recognized_token = ['if', 'else', '==', '<=', '>=', '&&', '||'] # daftar token yang sudah dikenali

    for char in clean_sentence: 
        buffered = ''.join(buffer) # menggabungkan token yang sudah dibuffer
        if buffered in recognized_token: # jika token sudah dikenali
            for i in range(len(buffered)): # menghapus token yang sudah dibuffer
                ordered_token.pop(-1) 
            ordered_token.append(buffered) # menambahkan token yang sudah dikenali

        ordered_token.append(char) # menambahkan token yang belum dikenali

        buffer.append(char) # menambahkan token ke buffer

        if char == ' ': # jika token adalah spasi
            buffer.clear() # mengosongkan buffer
    ordered_token.append('#') # menambahkan token akhir

    return [ordered_token, clean_sentence] # mengembalikan daftar token yang sudah diurutkan dan daftar token yang sudah dibersihkan
