class Queue:
    def __init__(self, q=None) -> None:
        self._queue = q.copy() if q else []
    
    def __repr__(self) -> str:
        return str(self._queue)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._queue[0]
    
    def poll(self):
        if self.is_empty():
            raise IndexError("poll from empty queue")
        return self._queue.pop(0)
    
    def offer(self, e) -> None:
        self._queue.append(e)
    
    def is_empty(self) -> bool:
        return len(self._queue) == 0
    
    def clear(self) -> None:
        self._queue.clear()
    
    def __len__(self) -> int:
        return len(self._queue)