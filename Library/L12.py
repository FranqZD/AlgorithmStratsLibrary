from typing import TypeVar, Callable

T = TypeVar("T")

def binary_search(A: list[T], e: T, key: Callable = lambda x: x):
    def binary_search_rec(A, p, r, e):
        if p > r:
            return -1
        q = (p + r) // 2
        if key(A[q]) == e:
            return q
        elif key(A[q]) < e:
            return binary_search_rec(A, q + 1, r, e)
        else:
            return binary_search_rec(A, p, q - 1, e)

    return binary_search_rec(A, 0, len(A) - 1, e)

if __name__ == "__main__":
    A = [-5, 0, 1, 13, 21, 46, 99, 101, 102, 200]
    print(binary_search(A, 21))  # 4
    print(binary_search(A, 22))  # -1
    print(binary_search(A, 200)) # 9
