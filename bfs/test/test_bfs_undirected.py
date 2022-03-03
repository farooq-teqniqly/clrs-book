from bfs.graph import Graph, PersonNode, BFS

graph = Graph(False)
graph.add_edge(PersonNode("me"), PersonNode("bob"))
graph.add_edge(PersonNode("me"), PersonNode("alice"))
graph.add_edge(PersonNode("me"), PersonNode("claire"))
graph.add_edge(PersonNode("bob"), PersonNode("anuj"))
graph.add_edge(PersonNode("bob"), PersonNode("peggy"))
graph.add_edge(PersonNode("alice"), PersonNode("peggy"))
graph.add_edge(PersonNode("claire"), PersonNode("thom"))
graph.add_edge(PersonNode("claire"), PersonNode("jonny"))

searcher = BFS(graph)


def test_bfs_from_anuj():
    distance_table = searcher.search("anuj")

    assert distance_table["me"][1] == 2
    assert distance_table["bob"][1] == 1
    assert distance_table["alice"][1] == 3
    assert distance_table["claire"][1] == 3
    assert distance_table["anuj"][1] == 0
    assert distance_table["peggy"][1] == 2
    assert distance_table["thom"][1] == 4
    assert distance_table["jonny"][1] == 4
