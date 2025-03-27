#E08.1: Implementar un método que ordene un arreglo de cadenas de texto utilizando una cola de prioridad

def pgSort(strArray: list[str]) -> None:
    # Min-Heap
    def heapify(arr, n, i):
        min = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] < arr[min]:
            min = l

        if r < n and arr[r] < arr[min]:
            min = r

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            heapify(arr, n, min)

    # Heap Build
    n = len(strArray)
    for i in range(n // 2 - 1, -1, -1):
        heapify(strArray, n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        strArray[i], strArray[0] = strArray[0], strArray[i]
        heapify(strArray, i, 0)

    # La cola de prioridad ordena de menor a mayor, pero queremos orden ascendente
    # así que no necesitamos hacer nada más
