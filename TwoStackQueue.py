import time

class Stack:
    def __init__(self):
        self.items = []
     
    def is_empty(self):
        return len(self.items) == 0
     
    def push(self, item):
        self.items.append(item)
     
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()
     

class QueueStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, item):
        self.stack1.push(item)
    
    def dequeue(self):
        if self.stack2.is_empty():
            if self.stack1.is_empty():
                raise Exception("Queue is empty")
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    
    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()


# Función para medir tiempos de ejecución
def analyze_performance(n):
    queue = QueueStack()
    
    # Medir tiempo de enqueue
    start_time = time.time()
    for i in range(n):
        queue.enqueue(i)
    enqueue_time = time.time() - start_time

    # Medir tiempo de dequeue
    start_time = time.time()
    for i in range(n):
        queue.dequeue()
    dequeue_time = time.time() - start_time

    print(f"\nAnálisis de tiempos para {n} operaciones:")
    print(f"Tiempo de enqueue: {enqueue_time:.6f} segundos")
    print(f"Tiempo de dequeue: {dequeue_time:.6f} segundos")


analyze_performance(100)
analyze_performance(10)
analyze_performance(1000)
analyze_performance(10000)
