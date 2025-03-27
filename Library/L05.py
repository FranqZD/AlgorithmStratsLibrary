class Stack:
    def __init__(self, s=None) -> None:
        self._stack = s.copy() if s else []
    
    def __repr__(self) -> str:
        return str(self._stack)
    
    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._stack[-1]
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._stack.pop()
    
    def push(self, e) -> None:
        self._stack.append(e)
    
    def is_empty(self) -> bool:
        return len(self._stack) == 0
    
    def clear(self) -> None:
        self._stack.clear()
    
    def __len__(self) -> int:
        return len(self._stack)