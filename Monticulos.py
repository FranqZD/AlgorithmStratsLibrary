# Implementa una cola de prioridad basada en monticulos binarios
# y utilizala para generar una funcion que ordene un arreglo de cadenas de texto
class Max_Heap:
    def _init_(self):
        self.heap = []

    # Define al nodo padre
    def parent(self, i):
        return (i - 1) // 2

    # Define al nodo izquierdo
    def left_child(self, i):
        return 2 * i + 1

    # Define al nodo derecho
    def right_child(self, i):
        return 2 * i + 2

    # Ordena el monticulo maximo segun el nodo i
    def heapify(self, i):
        big = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[big]:
            big = left
        if right < len(self.heap) and self.heap[right] > self.heap[big]:
            big = right
        if big != i:
            self.heap[i], self.heap[big] = self.heap[big], self.heap[i]
            self.heapify(big)

    # Agrega y ordena un nuevo elemento
    def insert(self, element):
        self.heap.append(element)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Obtiene el elemento raiz
    def get_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return max_val

    def is_empty(self):
        return len(self.heap) == 0

# Funcion que agrega y ordena las cadenas de texto
def ord_texto(palabras):
    array_ord = []
    heap = Max_Heap()

    for letra in palabras:
        heap.insert(letra)

    while not heap.is_empty():
        array_ord.append(heap.get_max())

    return array_ord[::-1]

# Ejemplos de ejecucion
helados = ['Vainilla', 'Chocolate', 'Menta', 'Oreo']
ordenar = ord_texto(helados)
print(ordenar)

nombres = ['Natalia', 'Francisco', 'Luis', 'Paulina']
order = ord_texto(nombres)
print(order)