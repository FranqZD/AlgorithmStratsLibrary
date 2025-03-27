from enum import Enum
from typing import TypeVar, Callable, List
T = TypeVar("T")

def parent(i: int) -> int:
    return i // 2

def left(i: int) -> int:
    return i * 2

def right(i: int) -> int:
    return (i * 2) + 1

class HeapType(Enum):
    MAX = 0
    MIN = 1

class Heap:
    def __init__(
        self,
        A: List[T],
        heapType: HeapType = HeapType.MAX,
        key: Callable[[T], any] = lambda x: x,
    ) -> None:
        self._heap = [None] + list(A)  # Make the array 1-indexed
        self._key = key
        self.heap_size = len(A)
        self.type = heapType
        self.build_heap()

    def __repr__(self) -> str:
        return str(self._heap[1 : self.heap_size + 1])

    def _compare(self, a: T, b: T) -> bool:
        if self.type == HeapType.MAX:
            return self._key(a) >= self._key(b)
        else:
            return self._key(a) <= self._key(b)

    def assert_heap_property(self) -> None:
        for i in range(2, self.heap_size + 1):
            if not self._compare(self._heap[parent(i)], self._heap[i]):
                raise AssertionError(
                    f"Heap property violated at index {i}: "
                    f"parent {self._heap[parent(i)]}, child {self._heap[i]}"
                )

    def heapify(self, i: int) -> None:
        l = left(i)
        r = right(i)
        selected = i

        if l <= self.heap_size and not self._compare(self._heap[selected], self._heap[l]):
            selected = l
        if r <= self.heap_size and not self._compare(self._heap[selected], self._heap[r]):
            selected = r

        if selected != i:
            self._heap[i], self._heap[selected] = self._heap[selected], self._heap[i]
            self.heapify(selected)

    def build_heap(self) -> None:
        for i in range(self.heap_size // 2, 0, -1):
            self.heapify(i)

    def get_heap(self) -> List[T]:
        return self._heap[1 : self.heap_size + 1]

    def push(self, item: T) -> None:
        self.heap_size += 1
        if len(self._heap) <= self.heap_size:
            self._heap.append(item)
        else:
            self._heap[self.heap_size] = item
        
        i = self.heap_size
        while i > 1 and not self._compare(self._heap[parent(i)], self._heap[i]):
            self._heap[i], self._heap[parent(i)] = self._heap[parent(i)], self._heap[i]
            i = parent(i)

    def pop(self) -> T:
        if self.heap_size < 1:
            raise IndexError("pop from empty heap")
        
        root = self._heap[1]
        self._heap[1] = self._heap[self.heap_size]
        self.heap_size -= 1
        self.heapify(1)
        return root

    def peek(self) -> T:
        if self.heap_size < 1:
            raise IndexError("peek from empty heap")
        return self._heap[1]

    def size(self) -> int:
        return self.heap_size

    def is_empty(self) -> bool:
        return self.heap_size == 0

    @staticmethod
    def heapsort(A: List[T], key: Callable[[T], any] = lambda x: x, reverse: bool = False) -> None:
        heap_type = HeapType.MIN if reverse else HeapType.MAX
        heap = Heap(A, heap_type, key)
        
        for i in range(len(A), 0, -1):
            A[i-1] = heap.pop()