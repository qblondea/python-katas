import unicodedata
from collections import Counter

def _normalize(s: str) -> str:
    """
    Normalise une chaîne :
    - décomposition Unicode (NFD)
    - suppression des diacritiques (catégorie Mn)
    - passage en minuscules
    - conservation des seuls alphanumériques
    """
    s_nfd = unicodedata.normalize("NFD", s)
    no_diacritics = "".join(ch for ch in s_nfd if unicodedata.category(ch) != "Mn")
    return "".join(ch.lower() for ch in no_diacritics if ch.isalnum())


def is_anagram(a: str, b: str) -> bool:

    if a is None:
        return False
        
    a_norm = _normalize(a)
    b_norm = _normalize(b)
    
    if len(a_norm) != len(b_norm):
        return False

    return Counter(a_norm) == Counter(b_norm)

