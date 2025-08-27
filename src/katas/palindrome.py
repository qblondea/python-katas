import numpy as np
import unicodedata


"""PALINDROME"""

def is_palindrome_1(s: str) -> bool:

    # normalise unicode, retire diacritiques et passe en minuscule
    s_norm = unicodedata.normalize("NFD", s)
    s_norm = "".join(ch for ch in s_norm if unicodedata.category(ch) != "Mn")
    t = "".join(ch.lower() for ch in s_norm if ch.isalnum())

    palindrome = True

    i, j = 0, len(t) - 1
    while i < j:
        if t[i] != t[j]:
            palindrome = False
        i += 1
        j -= 1
    
    return palindrome 