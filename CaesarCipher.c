#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char *encrypt(const char *text, int key)
{
    int length = strlen(text);
    char *cipher = (char *)malloc((length + 1) * sizeof(char));
    if (cipher == NULL)
    {
        printf("Memory allocation error\n");
        exit(1);
    }
    int i = 0;
    while (text[i] != '\0')
    {
        if (isupper(text[i]))
            cipher[i] = ((text[i] + key - 65) % 26) + 65;
        else
            cipher[i] = ((text[i] + key - 97) % 26) + 97;
        i++;
    }
    cipher[i] = '\0';
    return cipher;
}

char *decrypt(const char *cipher, int key)
{
    int length = strlen(cipher);
    char *text = (char *)malloc((length + 1) * sizeof(char));
    if (text == NULL)
    {
        printf("Memory allocation error\n");
        exit(1);
    }
    int i = 0;
    while (cipher[i] != '\0')
    {
        if (isupper(cipher[i]))
            text[i] = ((cipher[i] - key - 65 + 26) % 26) + 65;
        else
            text[i] = ((cipher[i] - key - 97 + 26) % 26) + 97;
        i++;
    }
    text[i] = '\0';
    return text;
}

int main()
{
    if (system("clear") != 0)
    {
        system("cls");
    }

    char text[100];
    int key;

    printf("Enter text and key to encrypt: ");
    scanf("%s %d", text, &key);

    char *encryptedText = encrypt(text, key);
    char *originalMsg = decrypt(encryptedText, key);

    printf("The encrypted text is: %s\n", encryptedText);
    printf("The original message is: %s\n", originalMsg);

    free(encryptedText);
    free(originalMsg);

    return 0;
}
