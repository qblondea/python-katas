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
