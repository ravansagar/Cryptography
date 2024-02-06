import numpy as np

def partText(msg, dim):
    parts = []
    for i in range(0, len(msg), dim):
        subString = msg[i:i+dim]
        if len(subString) < dim:
            subString += 'X' * (dim - len(subString))
        parts.append(subString)
    return parts

def hillCipher(msg, key, mode = 'encrypt'):
    msgPadding = partText(msg,2);
    msgCode = np.array([[(ord(i.upper()) - 65) % 26 for i in msgPadding[j]] for j in range(len(msgPadding))])
    if mode == "encrypt":
        cipherKey = np.zeros_like(key)
        cipherText = ''
        for row in msgCode:
            cipherKey = np.append(cipherKey, np.dot(row, key)%26) 
        cipherKey = cipherKey.reshape(-1, 2)
        cipherKey = cipherKey[~np.all(cipherKey == 0, axis = 1)]
        for i in cipherKey:
            for j in i:
                cipherText += (chr(j+65))
        return cipherText
    
    elif mode == 'decrypt':
        plainKey = np.zeros_like(key)
        plainText = ''
        inverseMatrix = np.linalg.inv(key)
        determinant = round(np.linalg.det(inverseMatrix))
        mod = pow(determinant, -1, 26) * determinant
        decryptionKey = (inverseMatrix * mod) % 26
        for row in msgCode:
            plainKey = np.append(plainKey, np.dot(row, decryptionKey) % 26) 
        plainKey = plainKey.reshape(-1, 2)
        plainKey = plainKey[~np.all(plainKey == 0, axis = 1)]
        plainKey = np.round(plainKey).astype(int)
        print(type(plainKey[0][0]))
        print(plainKey)
        for i in plainKey:
            for j in i:   
                plainText += (chr(int(j)+65))
        return plainText

    else:
        print("Please select correct mode either encrypt or decrypt")
        main()
def main():
    msg, mode = input("Enter massage and method : ").split()
    dim = int(input("Enter dimension of key matrix : "))
    shape = (dim, dim)
    key = np.array(shape)
    for index in np.ndindex(*shape):
        value = input(f"Enter value for element {index}: ")
        key[index] = int(value)
    result = hillCipher(msg,key,mode)
    print(result)

if __name__ == "__main__":
    main()