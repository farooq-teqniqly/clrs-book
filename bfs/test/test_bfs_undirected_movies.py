from bfs.graph import Graph, Node, PersonNode, BFS


class MovieNode(Node):
    def __init__(self, name: str):
        super().__init__(name, {})


graph = Graph(False)
graph.add_edge(PersonNode("Uma Thurman"), MovieNode("Pulp Fiction"))
graph.add_edge(PersonNode("Uma Thurman"), MovieNode("Gattaca"))
graph.add_edge(PersonNode("Ethan Hawke"), MovieNode("Gattaca"))
graph.add_edge(PersonNode("Uma Thurman"), MovieNode("Pulp Fiction"))
graph.add_edge(PersonNode("John Travolta"), MovieNode("Pulp Fiction"))
graph.add_edge(PersonNode("Samuel Jackson"), MovieNode("Pulp Fiction"))
graph.add_edge(PersonNode("Samuel Jackson"), MovieNode("Jackie Brown"))
graph.add_edge(PersonNode("Robert DeNiro"), MovieNode("Jackie Brown"))
graph.add_edge(PersonNode("Briget Fonda"), MovieNode("Jackie Brown"))
graph.add_edge(PersonNode("Samuel Jackson"), MovieNode("Goodfellas"))
graph.add_edge(PersonNode("Joe Pesci"), MovieNode("Goodfellas"))
graph.add_edge(PersonNode("Ray Liotta"), MovieNode("Goodfellas"))
graph.add_edge(PersonNode("Ray Liotta"), MovieNode("Blow"))
graph.add_edge(PersonNode("Johnny Depp"), MovieNode("Blow"))
graph.add_edge(PersonNode("Johnny Depp"), MovieNode("Donnie Brasco"))
graph.add_edge(PersonNode("Johnny Depp"), MovieNode("Edward Scissorhands"))
graph.add_edge(PersonNode("Al Pacino"), MovieNode("Donnie Brasco"))
graph.add_edge(PersonNode("Al Pacino"), MovieNode("The Godfather"))


searcher = BFS(graph)


def test_bfs_from_node():
    distance_table = searcher.search("Uma Thurman")
    pass
