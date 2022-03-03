from bfs.graph import Graph, PersonNode


def test_directed_graph():
    graph = Graph()
    graph.add_edge(PersonNode("me"), PersonNode("bob"))
    graph.add_edge(PersonNode("me"), PersonNode("alice"))
    graph.add_edge(PersonNode("me"), PersonNode("claire"))
    graph.add_edge(PersonNode("bob"), PersonNode("anuj"))
    graph.add_edge(PersonNode("bob"), PersonNode("peggy"))
    graph.add_edge(PersonNode("alice"), PersonNode("peggy"))
    graph.add_edge(PersonNode("claire"), PersonNode("thom"))
    graph.add_edge(PersonNode("claire"), PersonNode("jonny"))

    my_neighbors = [node.key for node in graph.get_neighbors("me")]
    bob_neighbors = [node.key for node in graph.get_neighbors("bob")]
    alice_neighbors = [node.key for node in graph.get_neighbors("alice")]
    claire_neighbors = [node.key for node in graph.get_neighbors("claire")]
    anuj_neighbors = [node.key for node in graph.get_neighbors("anuj")]
    peggy_neighbors = [node.key for node in graph.get_neighbors("peggy")]
    jonny_neighbors = [node.key for node in graph.get_neighbors("jonny")]
    thom_neighbors = [node.key for node in graph.get_neighbors("thom")]

    assert my_neighbors == ["bob", "alice", "claire"]
    assert bob_neighbors == ["anuj", "peggy"]
    assert alice_neighbors == ["peggy"]
    assert claire_neighbors == ["thom", "jonny"]
    assert anuj_neighbors == []
    assert peggy_neighbors == []
    assert jonny_neighbors == []
    assert thom_neighbors == []


def test_undirected_graph():
    graph = Graph(False)
    graph.add_edge(PersonNode("me"), PersonNode("bob"))
    graph.add_edge(PersonNode("me"), PersonNode("alice"))
    graph.add_edge(PersonNode("me"), PersonNode("claire"))
    graph.add_edge(PersonNode("bob"), PersonNode("anuj"))
    graph.add_edge(PersonNode("bob"), PersonNode("peggy"))
    graph.add_edge(PersonNode("alice"), PersonNode("peggy"))
    graph.add_edge(PersonNode("claire"), PersonNode("thom"))
    graph.add_edge(PersonNode("claire"), PersonNode("jonny"))

    my_neighbors = [node.key for node in graph.get_neighbors("me")]
    bob_neighbors = [node.key for node in graph.get_neighbors("bob")]
    alice_neighbors = [node.key for node in graph.get_neighbors("alice")]
    claire_neighbors = [node.key for node in graph.get_neighbors("claire")]
    anuj_neighbors = [node.key for node in graph.get_neighbors("anuj")]
    peggy_neighbors = [node.key for node in graph.get_neighbors("peggy")]
    jonny_neighbors = [node.key for node in graph.get_neighbors("jonny")]
    thom_neighbors = [node.key for node in graph.get_neighbors("thom")]

    assert my_neighbors == ["bob", "alice", "claire"]
    assert bob_neighbors == ["me", "anuj", "peggy"]
    assert alice_neighbors == ["me", "peggy"]
    assert claire_neighbors == ["me", "thom", "jonny"]
    assert anuj_neighbors == ["bob"]
    assert peggy_neighbors == ["bob", "alice"]
    assert jonny_neighbors == ["claire"]
    assert thom_neighbors == ["claire"]
