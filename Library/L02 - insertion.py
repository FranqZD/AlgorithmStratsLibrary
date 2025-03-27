from typing import TypeVar, Callable

T = TypeVar("T")

def insertion_sort(
    A: list[T], key: Callable = lambda x: x, reverse: bool = False
) -> None:

    # Se empieza desde 1, porque no se puede ordenar un solo elemento
    for i in range(1, len(A)):
        current = A[i]
        j = i-1

        while j >= 0 and key(A[j]) > key(current):
            A[j+1] = A[j]
            j -= 1

        A[j+1] = current

    if reverse:
        A.reverse()

if __name__ == "__main__":

    A = [3, 2, 5, 1, 9, 0, 8, 6, 7, 4]
    insertion_sort(A)
    print(A)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    insertion_sort(A, reverse=True)
    print(A)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    B = [(3, 8), (2, 0), (5, 5), (1, 6), (9, 3), (0, 2), (8, 1), (6, 4), (7, 9), (4, 7)]
    insertion_sort(B)
    print(B)
    # [(0, 2), (1, 6), (2, 0), (3, 8), (4, 7), (5, 5), (6, 4), (7, 9), (8, 1), (9, 3)]
    insertion_sort(B, key=lambda x: x[1])
    print(B)
    # [(2, 0), (8, 1), (0, 2), (9, 3), (6, 4), (5, 5), (1, 6), (4, 7), (3, 8), (7, 9)]
