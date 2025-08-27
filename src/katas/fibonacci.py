# Suite de Fibonacci

def fibonacci(n:int) -> int:

    """
    Renvoie le n-ième nombre de Fibonacci (0-indexé).
    F(0)=0, F(1)=1, puis F(n)=F(n-1)+F(n-2) pour n>=2.

    Raises:
        TypeError: si n n'est pas un int.
        ValueError: si n < 0.
    """

    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be >= 0")
    
    A = [0,1]

    if n < 2:
        return A[n]
    
    else:
        for i in range(2, n + 1):
                A.append(A[i - 1] + A[i - 2])
        return A[len(A)-1]
