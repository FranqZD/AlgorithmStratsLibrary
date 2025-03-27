#P08.3: Implementar un método que calcule la moda de una lista de enteros, es
#decir, el elemento más frecuente.

def mode(intArray: list[int]) -> int:

    freq = {}
    count = 0
    mode = intArray[0]

    for num in intArray:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

        if freq[num] > count:
            count = freq[num]
            mode = num

    return mode
