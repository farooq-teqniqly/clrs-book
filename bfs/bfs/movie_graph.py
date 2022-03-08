from bfs.graph import Graph, Node, PersonNode


class MovieNode(Node):
    def __init__(self, name: str):
        super().__init__(name, {})


class MovieGraph(Graph):
    def __init__(self):
        super().__init__(False)

    def add_edge(self, node1: PersonNode, node2: MovieNode):
        if not isinstance(node1, PersonNode):
            raise ValueError(f"First parameter must be of type {type(PersonNode)}")

        if not isinstance(node2, MovieNode):
            raise ValueError(f"Second parameter must be of type {type(MovieNode)}")

        super(MovieGraph, self).add_edge(node1, node2)
