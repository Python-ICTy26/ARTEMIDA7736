def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                ciphertext += chr(
                    (ord(plaintext[i]) - 2 * ord('A') + ord(keyword[i % len(keyword)].upper())) % 26 + ord('A'))
            else:
                ciphertext += chr(
                    (ord(plaintext[i]) - 2 * ord('a') + ord(keyword[i % len(keyword)].lower())) % 26 + ord('a'))
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - ord(keyword[i % len(keyword)].upper())) % 26 + ord('A'))
            else:
                plaintext += chr((ord(ciphertext[i]) - ord(keyword[i % len(keyword)].lower())) % 26 + ord('a'))
        else:
            plaintext += ciphertext[i]
    return plaintext
