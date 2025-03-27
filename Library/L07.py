class List:
    def __init__(self, initial_list: list[any] = None) -> None:
        self._list = initial_list.copy() if initial_list else []
    
    def __repr__(self) -> str:
        return str(self._list)
    
    def add(self, e) -> None:
        self._list.append(e)
    
    def get(self, i: int):
        if i < 0 or i >= len(self._list):
            raise IndexError("list index out of range")
        return self._list[i]
    
    def remove(self, i: int):
        if i < 0 or i >= len(self._list):
            raise IndexError("list index out of range")
        return self._list.pop(i)
    
    def index_of(self, e) -> int:
        try:
            return self._list.index(e)
        except ValueError:
            return -1
    
    def size(self) -> int:
        return len(self._list)
    
    def __len__(self) -> int:
        return len(self._list)
    
    def clear(self) -> None:
        self._list.clear()
    
    def contains(self, e) -> bool:
        return e in self._list