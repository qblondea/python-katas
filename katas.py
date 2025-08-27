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

""" 
-----------------
---FACTORIELLE---
-----------------

0! = 1 par convention,
n doit être un entier ≥ 0,
sinon, on doit lever une erreur appropriée.
"""

def factorial_0(n: int)-> int:
    r = 1
    if n == 0:
        return 1
    else:
        for k in range(n):
            r *= k
        return r
    

def factorial(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result