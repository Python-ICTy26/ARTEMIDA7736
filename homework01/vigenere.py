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
    keylen = len(keyword)
    keymod = [ord(i) for i in keyword]
    plaintextmod = [ord(i) for i in plaintext]
    for i in range(len(plaintextmod)):
        result = (plaintextmod[i] + keymod[i % keylen]) % 26
        ciphertext += chr(result + 65)
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
    keylen = len(keyword)
    keymod = [ord(i) for i in keyword]
    ciphertextmod = [ord(i) for i in ciphertext]
    for i in range(len(ciphertextmod)):
        result = (ciphertextmod[i] - keymod[i % keylen]) % 26
        ciphertext += chr(result + 65)
    return plaintext
