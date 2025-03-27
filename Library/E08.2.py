#E08.2: Implementar un método que determine si un arreglo de palabras tiene alguna repetida.

def hasDuplicates(strArray: list[str]) -> bool:
    seen = set()
    for word in strArray:
        if word in seen:
            return True
        seen.add(word)
    return False