import string
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
    shift = shift % 26
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    table = str.maketrans(
        lower + upper,
        lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]
    )
    return plaintext.translate(table)


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
    return encrypt_caesar(ciphertext, -shift)


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    best_count = 0
    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)
        words = decrypted.lower().split()
        count = sum(1 for w in words if w.strip(".,!?;:") in dictionary)
        if count > best_count:
            best_count = count
            best_shift = shift
    return best_shift