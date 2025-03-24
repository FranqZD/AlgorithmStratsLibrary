from typing import TypeVar, Callable, List
T = TypeVar("T")

class Node:
    def __init__(self, key: T, parent=None, left=None, right=None) -> None:
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        self.key: T = key

    # DFS
    def __repr__(self, level=0) -> str:
        indent = " " * level
        repr_str = f"{indent}Node({self.key})"
        if self.left:
            repr_str += f"\n{self.left.__repr__(level + 1)}"
        if self.right:
            repr_str += f"\n{self.right.__repr__(level + 1)}"
        return repr_str

class BST:
    def __init__(self, root: Node = None) -> None:
        self.root = root
    
    def __repr__(self) -> str:
        return str(self.root)
    
    def assert_bst_property(self) -> bool:
        return self.__assert_bst_property(self.root)
    
    def __assert_bst_property(self, x: Node) -> bool:
        if x is None:
            return True
        if x.left and x.right:
            return (
                x.left.key <= x.key
                and x.right.key >= x.key
                and self.__assert_bst_property(x.left)
                and self.__assert_bst_property(x.right)
            )
        if x.left:
            return x.left.key <= x.key and self.__assert_bst_property(x.left)
        if x.right:
            return x.right.key >= x.key and self.__assert_bst_property(x.right)
        return True
    
    def in_order_walk(self) -> List[int]:
        return self.__in_order_walk(self.root)
    
    def __in_order_walk(self, x: Node) -> List[int]:
        if x is None:
            return []
        return self.__in_order_walk(x.left) + [x.key] + self.__in_order_walk(x.right)
    
    def search(self, k: int) -> bool:
        return self.__search(self.root, k) is not None
    
    def __search(self, x: Node, k: int) -> Node:
        if x is None or x.key == k:
            return x
        if k < x.key:
            return self.__search(x.left, k)
        else:
            return self.__search(x.right, k)
    
    def minimum(self) -> T:
        if self.root is None:
            raise ValueError("Tree is empty")
        return self.__minimum(self.root).key
    
    def __minimum(self, x: Node) -> Node:
        while x.left is not None:
            x = x.left
        return x
    
    def maximum(self) -> T:
        if self.root is None:
            raise ValueError("Tree is empty")
        return self.__maximum(self.root).key
    
    def __maximum(self, x: Node) -> Node:
        while x.right is not None:
            x = x.right
        return x
    
    def successor(self, k: T) -> T:
        x = self.__search(self.root, k)
        if x is None:
            raise ValueError("Key not found")
        s = self.__successor(x)
        return s.key if s is not None else None
    
    def __successor(self, x: Node) -> Node:
        if x.right is not None:
            return self.__minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y
    
    def predecessor(self, k: T) -> T:
        x = self.__search(self.root, k)
        if x is None:
            raise ValueError("Key not found")
        p = self.__predecessor(x)
        return p.key if p is not None else None
    
    def __predecessor(self, x: Node) -> Node:
        if x.left is not None:
            return self.__maximum(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y
    
    def insert(self, k: T) -> bool:
        return self.__insert(Node(k))
    
    def __insert(self, z: Node) -> bool:
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key == x.key:
                return False
            elif z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        return True
    
    def delete(self, k: T) -> bool:
        z = self.__search(self.root, k)
        if z is not None:
            self.__delete(z)
            return True
        return False
    
    def __delete(self, z: Node) -> None:
        if z.left is None:
            self.__transplant(z, z.right)
        elif z.right is None:
            self.__transplant(z, z.left)
        else:
            y = self.__minimum(z.right)
            if y.parent != z:
                self.__transplant(y, y.right)
                y.right = z.right
                if y.right is not None:
                    y.right.parent = y
            self.__transplant(z, y)
            y.left = z.left
            if y.left is not None:
                y.left.parent = y
    
    def __transplant(self, u: Node, v: Node) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

if __name__ == "__main__":
    t = BST()
    for i in [9, 5, 1, 0, 6, 3, 2, 4, 7, 8]:
        t.insert(i)
    print(t)
    # Node(9)
    #     Node(5)
    #         Node(1)
    #             Node(0)
    #             Node(3)
    #                 Node(2)
    #                 Node(4)
    #         Node(6)
    #             Node(7)
    #                 Node(8)
    print(t.in_order_walk())
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(t.assert_bst_property())
    # True
    print(t.search(10), t.search(9))
    # False, True
    print(t.minimum(), t.maximum())
    # 0, 9
    print(t.predecessor(5), t.successor(5))
    # 4, 6
    print(t.insert(10), t.assert_bst_property())
    # True, True
    print(t)
    # Node(9)
    #     Node(5)
    #         Node(1)
    #             Node(0)
    #             Node(3)
    #                 Node(2)
    #                 Node(4)
    #         Node(6)
    #             Node(7)
    #                 Node(8)
    #     Node(10)
    print(t.delete(5), t.assert_bst_property())
    # True, True
    print(t)
    # Node(9)
    #     Node(6)
    #         Node(1)
    #             Node(0)
    #             Node(3)
    #                 Node(2)
    #                 Node(4)
    #         Node(7)
    #             Node(8)
    #     Node(10)

