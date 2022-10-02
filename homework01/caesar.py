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
    sdvig = shift
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((ord(char) - ord("a") + sdvig) % 26 + ord("a"))
            else:
                ciphertext += chr((ord(char) - ord("A") + sdvig) % 26 + ord("A"))
        else:
            ciphertext += char
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
    sdvig = shift
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr((ord(char) - ord("a") - sdvig) % 26 + ord("a"))
            else:
                plaintext += chr((ord(char) - ord("A") - sdvig) % 26 + ord("A"))
        else:
            plaintext += char
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    if ciphertext in dictionary:
        return best_shift
    while best_shift <= 24:
        plaintext = decrypt_caesar(ciphertext, best_shift)
        if plaintext in dictionary:
            return best_shift
        best_shift += 1
    return best_shift
