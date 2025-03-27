from enum import Enum
from typing import List, Tuple, Callable

class HeapType(Enum):
    MAX = 1
    MIN = 2

class PriorityQueue:
    def __init__(self, A: List[Tuple[str, int]], queueType: HeapType, key: Callable):
        self.A = A[:]
        self.queueType = queueType
        self.key = key
        self.build_heap()
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def compare(self, a, b):
        return self.key(a) > self.key(b) if self.queueType == HeapType.MAX else self.key(a) < self.key(b)
    
    def heapify(self, i):
        l, r = self.left(i), self.right(i)
        extreme = i
        if l < len(self.A) and self.compare(self.A[l], self.A[extreme]):
            extreme = l
        if r < len(self.A) and self.compare(self.A[r], self.A[extreme]):
            extreme = r
        if extreme != i:
            self.A[i], self.A[extreme] = self.A[extreme], self.A[i]
            self.heapify(extreme)
    
    def build_heap(self):
        for i in range(len(self.A) // 2, -1, -1):
            self.heapify(i)
    
    def extremum(self):
        return self.A[0] if self.A else None
    
    def extract_extremum(self):
        if not self.A:
            return None
        extreme = self.A[0]
        self.A[0] = self.A[-1]
        self.A.pop()
        self.heapify(0)
        return extreme
    
    def upsert(self, e):
        for i in range(len(self.A)):
            if self.A[i][0] == e[0]:
                self.A[i] = e
                self.build_heap()
                return
        self.A.append(e)
        self.build_heap()

if __name__ == "__main__":
    A = [
        ("a", 4),
        ("b", 1),
        ("1", 3),
        ("Z", 2),
        ("@", 16),
        ("d", 9),
        ("A", 10),
        ("BB", 14),
        ("X", 8),
        ("-", 7),
    ]
    pq = PriorityQueue(A=A, queueType=HeapType.MAX, key=lambda x: x[1])
    print(pq.extremum())
    e = pq.extract_extremum()
    print(e)
    print(pq.A)
    pq.upsert(("@", 5))
    print(pq.A)
    pq.upsert(("@", 12))
    print(pq.A)
