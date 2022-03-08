import math
from collections import deque


class Node:
    def __init__(self, key: str, data: dict):
        self.key = key
        self.data = data

    def __hash__(self):
        hash_code = 997021164
        hash_code += hash_code * -1521134295 + hash(self.key)
        return hash_code


class PersonNode(Node):
    def __init__(self, name):
        super().__init__(name, {})


class Graph:
    def __init__(self, directed=True):
        self.adjacency_list = {}
        self.directed = directed

    def add_edge(self, node1: Node, node2: Node):
        if node1.key not in self.adjacency_list:
            self.adjacency_list[node1.key] = []

        if node2.key not in self.adjacency_list:
            self.adjacency_list[node2.key] = []

        self.adjacency_list[node1.key].append(node2)

        if not self.directed:
            self.adjacency_list[node2.key].append(node1)

    def get_neighbors(self, key: str):
        return self.adjacency_list[key]


class BFS:
    def __init__(self, graph: Graph):
        self.graph = graph

    def search(self, start_key: str) -> dict:
        distance_table = {}

        for key in [key for key in self.graph.adjacency_list.keys() if key != start_key]:
            distance_table[key] = ["w", math.inf, None]

        distance_table[start_key] = ["g", 0, None]

        queue = deque()
        queue.append(start_key)

        while queue:
            next_node = queue.popleft()
            for neighbor_node in self.graph.adjacency_list[next_node]:
                key = neighbor_node.key

                if distance_table[key][0] == "w":
                    distance_table[key][0] = "g"

                    if distance_table[key][1] == math.inf:
                        distance_table[key][1] = 1

                    distance_table[key][1] = distance_table[next_node][1] + 1

                    distance_table[key][2] = next_node
                    queue.append(neighbor_node.key)

            distance_table[next_node][0] = "b"

        return distance_table
