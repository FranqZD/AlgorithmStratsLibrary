from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, key: T, parent=None, left=None, right=None) -> None:
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        self.key: T = key

    # DFS:
    def __repr__(self, level=0):
        indent = "    " * level
        repr_str = f"{indent}Node(k={self.key}, h={self.height()}, bf={self.bf()})"
        if self.left:
            repr_str += f"\n{self.left.__repr__(level + 1)}"
        if self.right:
            repr_str += f"\n{self.right.__repr__(level + 1)}"
        return repr_str

    def height(self) -> int:
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.height() + 1
        if self.right is None:
            return self.left.height() + 1
        return max(self.right.height(), self.left.height()) + 1

    def bf(self) -> int:
        if self.left is None and self.right is None:
            return 0
        if self.left is None:
            return self.right.height()
        if self.right is None:
            return -self.left.height()
        return self.right.height() - self.left.height()


class AVL:
    def __init__(self, root: Node = None) -> None:
        self.root = root

    def __repr__(self) -> str:
        return str(self.root)

    def assert_bst_property(self) -> bool:
        if self.root:
            return self.__assert_bst_property(self.root)
        return True

    def __assert_bst_property(self, x: Node) -> bool:
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

    def assert_avl_property(self) -> bool:
        if self.root:
            return self.__assert_avl_property(self.root)
        return True

    def __assert_avl_property(self, x: Node) -> bool:
        if x.left and x.right:
            return (
                x.bf() in [-1, 0, 1]
                and self.__assert_avl_property(x.left)
                and self.__assert_avl_property(x.right)
            )
        if x.left:
            return x.bf() in [-1, 0, 1] and self.__assert_avl_property(x.left)
        if x.right:
            return x.bf() in [-1, 0, 1] and self.__assert_avl_property(x.right)
        return True

    def in_order_walk(self) -> list[T]:
        return self.__in_order_walk(self.root)

    def __in_order_walk(self, x: Node) -> list[T]:
        if x:
            return self.__in_order_walk(x.left) + [x.key] + self.__in_order_walk(x.right)
        return []

    def search(self, k: T) -> bool:
        return self.__search(self.root, k) is not None

    def __search(self, x: Node, k: T) -> Node:
        while x is not None and k != x.key:
            x = x.left if k < x.key else x.right
        return x

    def minimum(self) -> T:
        return self.__minimum(self.root).key

    def __minimum(self, x: Node) -> Node:
        while x.left is not None:
            x = x.left
        return x

    def maximum(self) -> T:
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
        if self.search(k):
            return False
        self.__insert(Node(k))
        return True

    def __insert(self, z: Node) -> None:
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
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
        self.__balance(z.parent)

    def delete(self, k: T) -> bool:
        z = self.__search(self.root, k)
        if z is not None:
            self.__delete(z)
            return True
        return False

    def __delete(self, z: Node) -> None:
        q = z.parent
        if z.left is None:
            self.__transplant(z, z.right)
        elif z.right is None:
            self.__transplant(z, z.left)
        else:
            y = self.__minimum(z.right)
            if y.parent != z:
                q = y.parent  
                self.__transplant(y, y.right)
                y.right = z.right
                if y.right is not None:
                    y.right.parent = y
            else:
                q = y  
            self.__transplant(z, y)
            y.left = z.left
            if y.left is not None:
                y.left.parent = y
        self.__balance(q)
        del z  

    def __transplant(self, u: Node, v: Node) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def __left_rotate(self, x: Node) -> Node:
        if x.right is None:
            raise Exception("Cannot left rotate")
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        return y

    def __right_rotate(self, y: Node) -> Node:
        if y.left is None:
            raise Exception("Cannot right rotate")
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        return x

    def __balance(self, y: Node):
        while y is not None:
            if y.bf() > 1:
                if y.right and y.right.bf() < 0:
                    self.__right_rotate(y.right)
                self.__left_rotate(y)
            elif y.bf() < -1:
                if y.left and y.left.bf() > 0:
                    self.__left_rotate(y.left)
                self.__right_rotate(y)
            y = y.parent


if __name__ == "__main__":

    t = AVL()
    for i in [9, 5, 1, 0, 6, 3, 2, 4, 7, 8]:
        t.insert(i)
    print(t)
    # Node(k=5, h=4, bf=0)
    #     Node(k=1, h=3, bf=1)
    #         Node(k=0, h=1, bf=0)
    #         Node(k=3, h=2, bf=0)
    #             Node(k=2, h=1, bf=0)
    #             Node(k=4, h=1, bf=0)
    #     Node(k=7, h=3, bf=1)
    #         Node(k=6, h=1, bf=0)
    #         Node(k=9, h=2, bf=-1)
    #             Node(k=8, h=1, bf=0)
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
    # Node(k=5, h=4, bf=0)
    #     Node(k=1, h=3, bf=1)
    #         Node(k=0, h=1, bf=0)
    #         Node(k=3, h=2, bf=0)
    #             Node(k=2, h=1, bf=0)
    #             Node(k=4, h=1, bf=0)
    #     Node(k=7, h=3, bf=1)
    #         Node(k=6, h=1, bf=0)
    #         Node(k=9, h=2, bf=0)
    #             Node(k=8, h=1, bf=0)
    #             Node(k=10, h=1, bf=0)
    print(t.delete(5), t.assert_bst_property())
    # True, True
    print(t)
    # Node(k=6, h=4, bf=0)
    #     Node(k=1, h=3, bf=1)
    #         Node(k=0, h=1, bf=0)
    #         Node(k=3, h=2, bf=0)
    #             Node(k=2, h=1, bf=0)
    #             Node(k=4, h=1, bf=0)
    #     Node(k=9, h=3, bf=-1)
    #         Node(k=7, h=2, bf=1)
    #             Node(k=8, h=1, bf=0)
    #         Node(k=10, h=1, bf=0)

