from hashlib import sha1, sha256

sha1hash = lambda text : sha1(text.encode('utf-8')).hexdigest()
sha2hash = lambda text : sha256(text.encode('utf-8')).hexdigest()

def main():
    text, mode = input("Enter text and mode (sha1 or sha2): ").split()
    if mode == 'sha1':
        print(sha1hash(text))
    elif mode == 'sha2':
        print(sha2hash(text))
    else:
        print("Incorrect mode!!!\n")
        main()

if __name__ == "__main__":
    main()