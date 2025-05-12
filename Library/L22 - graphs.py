from enum import Enum
from functools import total_ordering
from typing_extensions import Self
from collections import deque

class NodeColor(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2

@total_ordering
class Node:
    def __init__(self, value: str):
        self.value = value
        self.color = NodeColor.WHITE
        self.distance = float("inf")
        self.discovered = float("inf")
        self.finished = float("inf")
        self.parent: Node = None

    def __repr__(self) -> str:
        return str(self.value)

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

class GraphType(Enum):
    UNDIRECTED = 0
    DIRECTED = 1

class Graph:
    def __init__(self, type_: GraphType):
        self.type = type_
        self.V: dict[str, Node] = dict()
        self.E: set[tuple[Node, Node]] = set()
        self.Adj: dict[Node, set[Node]] = dict()

    def __repr__(self):
        return str(self.Adj)

    def get_node(self, s: int) -> Node:
        return self.V.get(s, None)

    def add_node(self, v: str):
        v_node = self.get_node(v)
        if not v_node:
            v_node = Node(v)
            self.V[v] = v_node
            self.Adj[v_node] = set()

    def add_edge(self, u: str, v: str):
        u = self.get_node(u)
        v = self.get_node(v)
        if u and v:
            self.E.add((u, v))
            self.Adj[u].add(v)
            if self.type == GraphType.UNDIRECTED:
                self.Adj[v].add(u)
        else:
            raise ValueError("Node not found in graph")

    def add_nodes(self, v_list: list[str]):
        for v in v_list:
            self.add_node(v)

    def add_edges(self, e_list: list[tuple[str, str]]):
        for e in e_list:
            self.add_edge(*e)

    def __reset_nodes(self):
        for v in self.V.values():
            v.color = NodeColor.WHITE
            v.distance = float("inf")
            v.discovered = float("inf")
            v.finished = float("inf")
            v.parent = None

    # Breadth First Search (BFS)
    def bfs(self, s: str) -> None:
        self.__reset_nodes()

        # Identifica el nodo inicial (s) y sus caracteristicas
        s_node = self.get_node(s)
        s_node.color = NodeColor.GRAY
        s_node.distance = 0
        s_node.parent = None
        # Cola que guarda los nodos recorridos
        q = deque([s_node])

        # Mientras la cola no este vacia...
        while q:
            # Saca el primer elemento de la cola
            u = q.popleft()
            for v in self.Adj[u]:
                # Si aun no se visita el nodo...
                if v.color == NodeColor.WHITE:
                    v.color = NodeColor.GRAY
                    v.distance = u.distance + 1
                    v.parent = u
                    # Se agrega a la cola
                    q.append(v)

            # Cambia el color a negro para indicar que ya fue visitado
            u.color = NodeColor.BLACK

    def get_bft(self, s: str) -> Self:
        # Creacion de un nuevo grafo
        G_pi = Graph(self.type)
        self.bfs(s)

        for v in self.V.values():
            # Se agregan los nodos de bfs a G_pi
            G_pi.add_node(v.value)

        # Si v tiene un padre se agrega una arista al nodo
        for v in self.V.values():
            if v.parent:
                G_pi.add_edge(v.parent.value, v.value)
        return G_pi

    def print_path(self, s: str, v: str) -> list[str]:
        # Nodos a utilizar (s es la raiz)
        s_node = self.get_node(s)
        v_node = self.get_node(v)

        # Si no hay nodos, no se hace nada
        if not s_node or not v_node:
            return []

        # Si no se tienen nodos padres, no se hace nada
        if v_node.parent is None and v_node != s_node:
            return []

        path = []
        while v_node:
            # Inserta el valor del nodo en path
            path.insert(0, v_node.value)
            # Cuando se llega a s se termina el grafo
            if v_node == s_node:
                break
            v_node = v_node.parent

        return path

    # Depth First Search (DFS)
    def dfs(self):
        self.__reset_nodes()
        time = 0

        for u in self.V.values():
            # Si aun no se visita un nodo...
            if u.color == NodeColor.WHITE:
                # Orden de nodos en dfs
               time = self.__dfs_visit(u, time)

    def __dfs_visit(self, u: Node, time: int, component=None):
        time += 1
        # Tiempo de descubrimiento de u
        u.discovered = time
        u.color = NodeColor.GRAY

        if component is not None:
            # Se agrega el nodo actual a la lista component
            component.append(u)

        for v in self.Adj[u]:
            if v.color == NodeColor.WHITE:
                # Se define u como padre de v
                v.parent = u
                time = self.__dfs_visit(v, time, component)
        # Se colorean de negro los nodos ya visitados
        u.color = NodeColor.BLACK

        # Se determina el tiempo del proceso
        time += 1
        u.finished = time
        return time

    # Tiene que ver con los tiempos de inicio y de fin
    def __classify_edges(self) -> dict[str, list[tuple[Node, Node]]]:
        # Diccionario con las clasificaciones
        classified_edges = {"tree": [], "back": [], "forward": [], "cross": []}

        for u, v in self.E:
            # Si v es padre de u, (u, v) son aristas del arbol
            if v.parent == u:
                classified_edges["tree"].append((u, v))
            # Si v fue descubierto antes que u, son aristas traseras
            elif v.discovered <= u.discovered and v.finished >= u.finished:
                classified_edges["back"].append((u, v))
            # Si u fue descubierto antes que v, son aristas delanteras
            elif u.discovered < v.discovered and u.finished > v.finished:
                classified_edges["forward"].append((u, v))
            else:
                classified_edges["cross"].append((u, v))
        return classified_edges

    def topological_sort(self) -> list[str]:
        # Comprueba que el grafo sea directo
        assert self.type == GraphType.DIRECTED, "Topological sort is not defined for undirected graphs"
        self.dfs()

        classified_edges = self.__classify_edges()
        # Si el grafo tiene una arista trasera, no se ejecuta
        if classified_edges["back"]:
            raise TypeError("Topological sort is not defined...")

        # Devuelve los nodos de mayor a menor
        sorted_nodes = sorted(self.V.values(), key=lambda  node: node.finished, reverse=True)
        return [node.value for node in sorted_nodes]

    # Funcion que se usa solo con scc
    def __dfs_visit_scc(self, u: Node, component: list[Node]):
        # Marca el nodo en gris
        u.color = NodeColor.GRAY
        # Agrega el nodo a component
        component.append(u)

        for v in self.Adj[u]:
            # Si el nodo no ha sido descubierto...
            if v.color == NodeColor.WHITE:
                self.__dfs_visit_scc(v, component)
        u.color = NodeColor.BLACK

    # Strongly Connected Components (SCC)
    def scc(self) -> list[list[str]]:
        # Aseguramos que el grafo sea dirigido
        assert (self.type == GraphType.DIRECTED), "SCC not supported or undirected graph"

        # 1. Llamar a DFS
        self.dfs()
        # 2. Construir el grafo transpuesto
        G_T = Graph(self.type)
        # Agregar los nodos al nuevo grafo
        G_T.add_nodes(self.V.keys())

        # Agregar las aristas al grafo en sentido contrario
        for u in self.V.values():
            for v in self.Adj[u]:
                G_T.add_edge(v.value, u.value)

        # Ordena los nodos
        sorted_nodes = sorted(self.V.values(), key=lambda u: u.finished, reverse=True)
        G_T.__reset_nodes()
        sccs = []

        # 3. Modificar DFS en orden decreciente sobre el grafo transpuesto
        for u in sorted_nodes:
            u_T = G_T.get_node(u.value)
            if u_T.color == NodeColor.WHITE:
                component = []
                G_T.__dfs_visit_scc(u_T, component)
                sccs.append([v.value for v in component])

        return sccs

if __name__ == "__main__":
    G = Graph(GraphType.DIRECTED)
    G.add_nodes(list("abcdefgh"))
    G.add_edges(
        [
            ("a", "b"),
            ("b", "c"),
            ("b", "e"),
            ("b", "f"),
            ("c", "d"),
            ("c", "g"),
            ("d", "c"),
            ("d", "h"),
            ("e", "a"),
            ("e", "f"),
            ("f", "g"),
            ("g", "f"),
            ("g", "h"),
            ("h", "h"),
        ]
    )
    print(G.Adj)
    # {a: {b}, b: {c, f, e}, c: {d, g}, d: {h, c}, e: {f, a}, f: {g}, g: {h, f}, h: {h}}
    G.bfs("a")
    for v in G.V.values():
        print(v, v.distance, v.parent)
    # a 0 None
    # b 1 a
    # c 2 b
    # d 3 c
    # e 2 b
    # f 2 b
    # g 3 c
    # h 4 g
    G.bfs("a")
    bft = G.get_bft("a")
    print(bft)
    # {g: {h}, f: {g}, a: {b}, h: set(), e: set(), d: set(), b: {c, f, e}, c: {d}}
    print(G.print_path("a", "h"))
    # ['a', 'b', 'c', 'g', 'h']
    G.dfs()
    for v in G.V.values():
        print(v.value, v.parent, v.discovered, v.finished)
    # a None 1 16
    # b a 2 15
    # c b 11 14
    # d c 12 13
    # e b 3 10
    # f e 4 9
    # g f 5 8
    # h g 6 7
    try:
        print(G.topological_sort())
        # TypeError: Topological sort is not defined for cyclic graphs.
    except:
        pass
    print(G._Graph__classify_edges())
    # Al correr el codigo a veces da forward = [] y a veces da forward = [(b, f)]
    # {'tree': [(a, b), (b, f), (b, c), (b, e), (c, d), (f, g), (g, h)], 'back': [(d, c), (e, a), (g, f), (h, h)], 'forward': [], 'cross': [(c, g), (d, h), (e, f)]}
    print(G.scc())
    # [['b', 'e', 'a'], ['d', 'c'], ['g', 'f'], ['h']]