def railFence(text, key, mode='encrypt'):
    text = text.replace(" ", "").upper()
    rails = [''] * key
    direction = -1 if mode == 'encrypt' else 1
    row = 0
    if mode == 'encrypt' or mode == 'e':
        for char in text:
            rails[row] += char
            if row == 0 or row == key - 1:
                direction *= -1
            row += direction

        return ''.join(rails)
    
    elif mode == 'decrypt' or mode == 'd':
        numChar = len(text)
        charIndex = 0
        lengths = [0] * key
        for i in range(numChar):
            lengths[abs(row)] += 1
            row += direction
            direction *= -1
        for i in range(key):
            rails[i] = text[charIndex: charIndex + lengths[i]]
            charIndex += lengths[i]
        direction = -1
        plainText = ''
        row = 0
        for i in range(numChar):
            plainText += rails[abs(row)][0]
            rails[abs(row)] = rails[abs(row)][1:]
            row += direction
            direction *= -1
        return plainText

    else:
        print("Incorrect mode it has to be either 'encrypt' or 'decrypt'")
        main()

def main():
    msg, mode = input("Enter msg and mode : ").split()
    key = int(input("Enter number of rails: "))
    result = railFence(msg, key, mode)
    print(result)
if __name__ == "__main__":
    main()