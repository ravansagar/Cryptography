prepare = lambda text: ''.join(filter(str.isalpha, text.upper()))
def keyMatrix(key):
    key = prepare(key)
    keyMatrix = ''.join(sorted(set(key), key=key.index))
    return keyMatrix + ''.join(filter(lambda x: x not in keyMatrix, 'ABCDEFGHIKLMNOPQRSTUVWXYZ'))

def splitText(text):
    pairs = []
    for i in range(0, len(text), 2):
        if i + 1 < len(text) and text[i] != text[i + 1]:
            pairs.append(text[i:i + 2])
        else:
            pairs.append(text[i] + 'X')
    return pairs

def playFair(text, key, mode='encrypt'):
    Matrix = keyMatrix(key)
    pairs = splitText(prepare(text))
    if mode == 'decrypt' or mode == 'd':
        Matrix = Matrix.replace('J', '')
        decryptedText = ''
        for pair in pairs:
            if len(pair) == 2:
                row1, col1 = divmod(Matrix.index(pair[0]), 5)
                row2, col2 = divmod(Matrix.index(pair[1]), 5)
                if row1 == row2:
                    decryptedText += Matrix[row1 * 5 + (col1 - 1) % 5] + Matrix[row2 * 5 + (col2 - 1) % 5]
                elif col1 == col2:
                    decryptedText += Matrix[((row1 - 1) % 5) * 5 + col1] + Matrix[((row2 - 1) % 5) * 5 + col2]
                else:
                    decryptedText += Matrix[row1 * 5 + col2] + Matrix[row2 * 5 + col1]
            else:
                decryptedText += pair
        return decryptedText
    elif mode == 'encrypt' or mode == 'e':
        cipherText = ''
        for pair in pairs:
            if len(pair) == 2:
                row1, col1 = divmod(Matrix.index(pair[0]), 5)
                row2, col2 = divmod(Matrix.index(pair[1]), 5)
                if row1 == row2:
                    cipherText += Matrix[row1 * 5 + (col1 + 1) % 5] + Matrix[row2 * 5 + (col2 + 1) % 5]
                elif col1 == col2:
                    cipherText += Matrix[((row1 + 1) % 5) * 5 + col1] + Matrix[((row2 + 1) % 5) * 5 + col2]
                else:
                    cipherText += Matrix[row1 * 5 + col2] + Matrix[row2 * 5 + col1]
            else:
                cipherText += pair
        return cipherText[0:len(text)]
    else:
        print("Incorrect mode it has to be either 'encrypt' or 'decrypt'")
        main()

def main():
    msg, key, mode = input("Enter text, key and mode (Separate with comma): ").split(",")
    print(playFair(msg, key, mode))

if __name__ == "__main__":
    main()