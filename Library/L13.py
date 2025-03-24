from typing import TypeVar, Callable
from collections import namedtuple
from functools import partial

T = TypeVar("T")
Customer = namedtuple("Customer", ["name", "rfc", "address"])

# HASH CODE FUNCTION FOR CUSTOMER OBJECTS
def hash_code(e: Customer, m: int) -> int:
    return hash(e.rfc) % m

class HashTable:
    def __init__(self, A: list[T], hash_code: Callable) -> None:
        self.table = {}
        self.hash_code = hash_code
        for e in A:
            self.insert(e)
    
    def __repr__(self) -> str:
        return str(self.table)
    
    def search(self, e: T) -> bool:
        index = self.hash_code(e)
        if index in self.table:
            return e in self.table[index]
        return False
    
    def insert(self, e: T) -> bool:
        index = self.hash_code(e)
        if index not in self.table:
            self.table[index] = [e]
            return True
        else:
            if e in self.table[index]:
                return False
            else:
                self.table[index].append(e)
                return True
    
    def delete(self, e: T) -> bool:
        index = self.hash_code(e)
        if index in self.table and e in self.table[index]:
            self.table[index].remove(e)
            if not self.table[index]:
                del self.table[index]
            return True
        return False

if __name__ == "__main__":
    with open("Clientes.txt", "r") as f:
        customers = [
            Customer(*[e.strip() for e in l.split("\t")]) for l in f.readlines()
        ]
    hc = partial(hash_code, m=len(customers))
    ht = HashTable(customers, hc)
    
    print(ht)
    print(ht.search(customers[0]))
    #True
    
    print(ht.insert(customers[0]))
    #False
    
    print(ht.delete(customers[0]))
    #True
    
    print(ht.delete(customers[0]))
    #False
    
    print(ht.insert(customers[0]))
    #True 
