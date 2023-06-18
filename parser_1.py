def parse(sentence):
    sentence = sentence.split('\n')

    clean_sentence = []
    for part in sentence:
        clean_sentence.append(part.strip())
    clean_sentence = "".join(clean_sentence)

    ordered_token = []
    buffer = []
    recognized_token = ['if', 'else', '==', '<=', '>=', '&&', '||']

    for char in clean_sentence:
        buffered = ''.join(buffer)
        if buffered in recognized_token:
            for i in range(len(buffered)):
                ordered_token.pop(-1)
            ordered_token.append(buffered)

        ordered_token.append(char)

        buffer.append(char)

        if char == ' ':
            buffer.clear()
    ordered_token.append('#')

    return [ordered_token, clean_sentence]
