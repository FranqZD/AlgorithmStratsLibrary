from typing import TypeVar, Callable

T = TypeVar("T")

def merge_sort(A: list[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    def merge(A, p, q, r):
        L = A[p:q + 1]
        R = A[q + 1:r + 1]
        i = j = 0
        k = p
        while i < len(L) and j < len(R):
            if key(L[i]) <= key(R[j]):
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    def merge_sort_rec(A, p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort_rec(A, p, q)
            merge_sort_rec(A, q + 1, r)
            merge(A, p, q, r)

    merge_sort_rec(A, 0, len(A) - 1)
    if reverse:
        A.reverse()

if __name__ == "__main__":
    A = [3, 2, 5, 1, 9, 0, 8, 6, 7, 4]
    merge_sort(A)
    print(A)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sort(A, reverse=True)
    print(A)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    B = [(3, 8), (2, 0), (5, 5), (1, 6), (9, 3), (0, 2), (8, 1), (6, 4), (7, 9), (4, 7)]
    merge_sort(B)
    print(B)  # [(0, 2), (1, 6), (2, 0), (3, 8), (4, 7), (5, 5), (6, 4), (7, 9), (8, 1), (9, 3)]
    merge_sort(B, key=lambda x: x[1])
    print(B)  # [(2, 0), (8, 1), (0, 2), (9, 3), (6, 4), (5, 5), (1, 6), (4, 7), (3, 8), (7, 9)]
