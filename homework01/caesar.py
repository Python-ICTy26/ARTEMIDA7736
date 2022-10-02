import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)): 
        char = plaintext[i] 
        if char.isupper(): 
            ciphertext += chr((ord(char) + shift - 1 - 64) % 26 + 65) 
        else: 
            ciphertext += chr((ord(char) + shift - 1 - 96) % 26 + 97) 
        if shift == 0:
            ciphertext = plaintext
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isupper():
            plaintext += chr((ord(char) - shift - 1 - 64) % 26 + 65)
        else:
            plaintext += chr((ord(char) - shift - 1 - 96) % 26 + 97)
        if shift == 0:
            plaintext=ciphertext
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    if ciphertext in dictionary:
        return best_shift
    while best_shift <= 24:
        plaintext = decrypt_caesar(ciphertext, best_shift)
        if plaintext in dictionary:
            return best_shift
        best_shift += 1
    return best_shift
