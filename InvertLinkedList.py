class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next  # Guarda el siguiente nodo
            curr.next = prev  # Invierte el enlace
            prev = curr  # Mueve prev a curr
            curr = next_node  # Avanza curr

        self.head = prev  # Nuevo head es el último nodo procesado

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


# 🔹 Prueba del algoritmo
if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)

    print("Lista original:")
    ll.print_list()

    ll.reverse()

    print("Lista invertida:")
    ll.print_list()
