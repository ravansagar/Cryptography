def caesarCipher(text, key=2, mode="encrypt"):
    if mode == "encrypt" or mode == 'e':
        cipher = []
        for i in text:
            if i == " ":
                cipher.append(i)
            elif i.isupper():
                cipher.append(chr((ord(i) + key - 65) % 26 + 65))
            else:
                cipher.append(chr((ord(i) + key - 97) % 26 + 97))
        return ''.join(cipher)
    elif mode == "decrypt" or mode == 'd':
        msg = []
        for i in text:
            if i == " ":
                msg.append(i)
            elif i.isupper():
                msg.append(chr((ord(i) - key - 65) % 26 + 65))
            else:
                msg.append(chr((ord(i) - key - 97) % 26 + 97))
        return ''.join(msg)
    else:
        print("Incorrect mode it has to be either 'encrypt' or 'decrypt'")
        main()

def main():
    msg, key, mode = input("Enter text, key and mode (Separate with comma): ").split(",")
    print(caesarCipher(msg, int(key), mode))

if __name__ == "__main__":
    main()