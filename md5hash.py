from hashlib import md5

def main():
    hash = lambda text : md5(text.encode('utf-8')).hexdigest()
    text = input("Enter text : ")
    print(f"Plain text : {text} \nHashed Text : {hash(text)}")

if __name__ == "__main__":
    main()