import time
from collections import deque

class QueueStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, item):
        """Inserta un elemento en la pila"""
        self.queue1.append(item)

    def pop(self):
        """Elimina y devuelve el último elemento apilado"""
        if not self.queue1:
            raise Exception("Stack is empty")

        # Pasamos todos los elementos menos el último a queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        popped_value = self.queue1.popleft()

        # Intercambiamos queue1 y queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_value

    def is_empty(self):
        """Verifica si la pila está vacía"""
        return not self.queue1


# Función para medir tiempos de ejecución
def analyze_performance(n):
    stack = QueueStack()

    # Medir tiempo de push
    start_time = time.time()
    for i in range(n):
        stack.push(i)
    push_time = time.time() - start_time

    # Medir tiempo de pop
    start_time = time.time()
    for i in range(n):
        stack.pop()
    pop_time = time.time() - start_time

    print(f"\nAnálisis de tiempos para {n} operaciones:")
    print(f"Tiempo de push: {push_time:.6f} segundos")
    print(f"Tiempo de pop: {pop_time:.6f} segundos")

# Pruebas con diferentes tamaños de operaciones
if __name__ == "__main__":
    analyze_performance(10)
    analyze_performance(100)
    analyze_performance(1000)
    analyze_performance(10000)
