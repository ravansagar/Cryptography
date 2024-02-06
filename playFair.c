#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#define SIZE 5 

char* encrypt(const char *plainText, const char key[SIZE][SIZE]) {
    int len = strlen(plainText);
    char *cipherText = (char*)malloc(len * sizeof(char) + 1); 
    if (cipherText == NULL) {
        printf("Memory allocation error\n");
        exit(1);
    }
    int i, j, index = 0;
    char ch1, ch2;
    for (i = 0; i < len; i += 2) {
        ch1 = plainText[i];
        ch2 = (i + 1 < len) ? plainText[i + 1] : 'X'; 
        if (ch1 == ch2) ch2 = 'X';
        int row1 = -1, col1 = -1, row2 = -1, col2 = -1;
        for (j = 0; j < SIZE && (row1 == -1 || row2 == -1); j++) {
            if (row1 == -1 && strchr(key[j], ch1)) {
                row1 = j;
                col1 = strchr(key[j], ch1) - key[j];
            }
            if (row2 == -1 && strchr(key[j], ch2)) {
                row2 = j;
                col2 = strchr(key[j], ch2) - key[j];
            }
        }
        if (row1 == row2) { 
            cipherText[index++] = key[row1][(col1 + 1) % SIZE];
            cipherText[index++] = key[row2][(col2 + 1) % SIZE];
        } else if (col1 == col2) {
            cipherText[index++] = key[(row1 + 1) % SIZE][col1];
            cipherText[index++] = key[(row2 + 1) % SIZE][col2];
        } else { 
            cipherText[index++] = key[row1][col2];
            cipherText[index++] = key[row2][col1];
        }
    }
    cipherText[index] = '\0';
    return cipherText;
}

char* decrypt(const char *cipherText, const char key[SIZE][SIZE]) {
    int len = strlen(cipherText);
    char *plainText = (char*)malloc(len * sizeof(char)); // Allocate memory for plaintext
    if (plainText == NULL) {
        printf("Memory allocation error\n");
        exit(1);
    }
    int i, row1, col1, row2, col2;
    for (i = 0; i < len; i += 2) {
        char ch1 = cipherText[i];
        char ch2 = cipherText[i + 1];
        findPosition(key, ch1, &row1, &col1);
        findPosition(key, ch2, &row2, &col2);
        if (row1 == row2) {
            plainText[i] = key[row1][(col1 - 1 + SIZE) % SIZE];
            plainText[i + 1] = key[row2][(col2 - 1 + SIZE) % SIZE];
        } else if (col1 == col2) { 
            plainText[i] = key[(row1 - 1 + SIZE) % SIZE][col1];
            plainText[i + 1] = key[(row2 - 1 + SIZE) % SIZE][col2];
        } else {
            plainText[i] = key[row1][col2];
            plainText[i + 1] = key[row2][col1];
        }
    }
    plainText[i] = '\0';
    return plainText;
}

int main() {
    char key[SIZE][SIZE] = {
        {'P', 'L', 'A', 'Y', 'F'},
        {'I', 'R', 'E', 'X', 'M'},
        {'B', 'C', 'D', 'G', 'H'},
        {'K', 'N', 'O', 'Q', 'S'},
        {'T', 'U', 'V', 'W', 'Z'}
    };
    char plainText[100];
    printf("Enter msg to encrypt : ");
    scanf("%s",plainText);
    char *ciphertext = encrypt(plainText, key);
    printf("Encrypted text: %s\n", ciphertext);
    free(ciphertext); 
    return 0;
}
